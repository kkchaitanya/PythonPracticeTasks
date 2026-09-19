from datetime import date, datetime
from uuid import UUID as PyUUID, uuid4
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# IMPORT YOUR CONFIG NEWLY CREATED HERE
from config import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship,selectinload
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, UniqueConstraint, UUID, Text,select

# ---------------------------------------------------------
# DATABASE CONFIGURATION & CONNECTION
# ---------------------------------------------------------
DATABASE_URL = settings.ASYNC_DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
# async_sessionmaker is the standard async factory in SQLAlchemy 2.0+
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Dependency to yield database sessions to API routes
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# ---------------------------------------------------------
# 2. SQLALCHEMY MODELS (Database Tables)
# ---------------------------------------------------------
class StudentDB(Base):
    __tablename__ = "students"

    student_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    enrollments = relationship("EnrollmentDB", back_populates="student", cascade="all, delete-orphan")


class CourseDB(Base):
    __tablename__ = "courses"

    course_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    course_code = Column(String(10), unique=True, nullable=False, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)  # Using SQLAlchemy's Text
    credits = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    enrollments = relationship("EnrollmentDB", back_populates="course", cascade="all, delete-orphan")


class EnrollmentDB(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.student_id", ondelete="CASCADE"), nullable=False)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.course_id", ondelete="CASCADE"), nullable=False)
    semester = Column(String(20), nullable=False)
    enrollment_date = Column(Date, default=date.today)
    grade = Column(String(2), nullable=True)

    student = relationship("StudentDB", back_populates="enrollments")
    course = relationship("CourseDB", back_populates="enrollments")

    __table_args__ = (
        UniqueConstraint('student_id', 'course_id', 'semester', name='unique_student_course_semester'),
    )

# ---------------------------------------------------------
# 3. PYDANTIC SCHEMAS (Data Validation & Serialization)
# ---------------------------------------------------------
class StudentCreate(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    date_of_birth: date

class EnrollmentCreate(BaseModel):
    student_id: PyUUID  # Uses Python's standard uuid.UUID
    course_id: PyUUID
    semester: str = Field(..., max_length=20)

class CourseCreate(BaseModel):
    course_code: str = Field(..., min_length=2, max_length=10, examples=["CS101"])
    title: str = Field(..., min_length=3, max_length=150, examples=["Introduction to Computer Science"])
    description: str | None = Field(None, examples=["Learn the fundamentals of programming using Python."])
    credits: int = Field(..., gt=0, le=6, description="Course credits must be between 1 and 6")
class StudentResponse(BaseModel):
    student_id: PyUUID
    first_name: str
    last_name: str
    email: EmailStr
    date_of_birth: date
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CourseResponse(BaseModel):
    course_id: PyUUID
    course_code: str
    title: str
    description: str | None
    credits: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class StudentSummary(BaseModel):
    student_id: PyUUID
    first_name: str
    last_name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class CourseSummary(BaseModel):
    course_id: PyUUID
    course_code: str
    title: str
    credits: int

    model_config = ConfigDict(from_attributes=True)

class EnrollmentResponse(BaseModel):
    enrollment_id: PyUUID
    semester: str
    enrollment_date: date
    grade: str | None
    student: StudentSummary
    course: CourseSummary

    model_config = ConfigDict(from_attributes=True)
# ---------------------------------------------------------
# 4. FASTAPI APP & WRITE OPERATIONS
# ---------------------------------------------------------
app = FastAPI(title="Neon University API")

@app.post("/students/", status_code=status.HTTP_201_CREATED)
async def create_student(student_data: StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = StudentDB(
        first_name=student_data.first_name,
        last_name=student_data.last_name,
        email=student_data.email,
        date_of_birth=student_data.date_of_birth
    )
    try:
        db.add(new_student)
        await db.flush()
        return {"message": "Student created successfully", "student_id": new_student.student_id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}"
        )

@app.post("/courses/", status_code=status.HTTP_201_CREATED)
async def course(course_data: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = CourseDB(
        course_code=course_data.course_code,
        title=course_data.title,
        description=course_data.description,
        credits=course_data.credits
    )
    try:
        db.add(new_course)
        await db.flush()
        return {"message": "Course created successfully", "course_id": new_course.course_id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}"
        )

@app.post("/enrollments/", status_code=status.HTTP_201_CREATED)
async def enroll_student(enrollment_data: EnrollmentCreate, db: AsyncSession = Depends(get_db)):
    new_enrollment = EnrollmentDB(
        student_id=enrollment_data.student_id,
        course_id=enrollment_data.course_id,
        semester=enrollment_data.semester
    )
    try:
        db.add(new_enrollment)
        await db.flush()
        return {"message": "Enrollment recorded successfully", "enrollment_id": new_enrollment.enrollment_id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Enrollment failed. Student may already be registered for this course this semester."
        )
    
@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: PyUUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(StudentDB).where(StudentDB.student_id == student_id))
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID '{student_id}' not found",
        )
    return student

@app.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: PyUUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseDB).where(CourseDB.course_id == course_id))
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID '{course_id}' not found",
        )
    return student

@app.get("/students/{student_id}/enrollments", response_model=list[EnrollmentResponse])
async def get_student_enrollments(student_id: PyUUID, db: AsyncSession = Depends(get_db)):
    query = (
        select(EnrollmentDB)
        .where(EnrollmentDB.student_id == student_id)
        .options(
            selectinload(EnrollmentDB.student),
            selectinload(EnrollmentDB.course)
        )
    )
    result = await db.execute(query)
    return result.scalars().all()

@app.get("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
async def get_enrollment(enrollment_id: PyUUID, db: AsyncSession = Depends(get_db)):
    query = (
        select(EnrollmentDB)
        .where(EnrollmentDB.enrollment_id == enrollment_id)
        .options(
            selectinload(EnrollmentDB.student),
            selectinload(EnrollmentDB.course)
        )
    )
    result = await db.execute(query)
    enrollment = result.scalar_one_or_none()

    if not enrollment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Enrollment with ID '{enrollment_id}' not found"
        )
    return enrollment

@app.get("/enrollments/", response_model=list[EnrollmentResponse])
async def list_enrollments(
    semester: str | None = None,
    skip: int = 0,
    limit: int = 50,
    db: AsyncSession = Depends(get_db)
):
    query = (
        select(EnrollmentDB)
        .options(
            selectinload(EnrollmentDB.student),
            selectinload(EnrollmentDB.course)
        )
        .offset(skip)
        .limit(limit)
    )

    if semester:
        query = query.where(EnrollmentDB.semester == semester)

    result = await db.execute(query)
    return result.scalars().all()