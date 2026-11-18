#import uuid 
from datetime import date, datetime
from tkinter.tix import TEXT
from uuid import  uuid4
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field

# IMPORT YOUR CONFIG NEWLY CREATED HERE
from config import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, UniqueConstraint,UUID

# ---------------------------------------------------------
# DATABASE CONFIGURATION & CONNECTION (UPDATED)
# ---------------------------------------------------------
# .unicode_string() converts Pydantic's specialized URL type back to a clean string
# Use the explicitly forced async URL property
DATABASE_URL = settings.ASYNC_DATABASE_URL

# Create your async engine normally
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
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
        finally:
            await session.close()

# ---------------------------------------------------------
# 2. SQLALCHEMY MODELS (Database Tables)
# ---------------------------------------------------------
# 1. STUDENTS MODEL
class StudentDB(Base):
    __tablename__ = "students"
    # FIX: Removed (as_uuid=True). It natively expects UUID objects now.
    student_id = Column(UUID, primary_key=True, default=uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    enrollments = relationship("EnrollmentDB", back_populates="student", cascade="all, delete-orphan")


# 2. COURSES MODEL
class CourseDB(Base):
    __tablename__ = "courses"
    
    # FIX: Cleaned UUID layout
    course_id = Column(UUID, primary_key=True, default=uuid4)
    course_code = Column(String(10), unique=True, nullable=False, index=True)
    title = Column(String(150), nullable=False)
    description = Column(TEXT, nullable=True)
    credits = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    enrollments = relationship("EnrollmentDB", back_populates="course", cascade="all, delete-orphan")


# 3. ENROLLMENTS MODEL
class EnrollmentDB(Base):
    __tablename__ = "enrollments"
    
    # FIX: Cleaned UUID and Foreign Key layouts
    enrollment_id = Column(UUID, primary_key=True, default=uuid4)
    
    student_id = Column(UUID, ForeignKey("students.student_id", ondelete="CASCADE"), nullable=False)
    course_id = Column(UUID, ForeignKey("courses.course_id", ondelete="CASCADE"), nullable=False)
    
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
    student_id: UUID
    course_id: UUID
    semester: str = Field(..., max_length=20)

class CourseCreate(BaseModel):
    course_code: str = Field(..., min_length=2, max_length=10, examples=["CS101"])
    title: str = Field(..., min_length=3, max_length=150, examples=["Introduction to Computer Science"])
    description: str | None = Field(None, examples=["Learn the fundamentals of programming using Python."])
    credits: int = Field(..., gt=0, le=6, description="Course credits must be between 1 and 6")


# ---------------------------------------------------------
# 4. FASTAPI APP & WRITE OPERATIONS
# ---------------------------------------------------------
app = FastAPI(title="Neon University API")

@app.post("/students/", status_code=status.HTTP_201_CREATED)
async def create_student(student_data: StudentCreate, db: AsyncSession = Depends(get_db)):
    """
    Write Operation: Creates a new student record in Neon.
    """
    new_student = StudentDB(
        first_name=student_data.first_name,
        last_name=student_data.last_name,
        email=student_data.email,
        date_of_birth=student_data.date_of_birth
    )
    
    try:
        db.add(new_student)
        await db.flush() # Flushes data to database to trigger constraints/generate defaults
        return {"message": "Student created successfully", "student_id": new_student.student_id}
    except Exception as e:
        # Handles cases like Duplicate Email errors cleanly
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}"
        )
@app.post("/courses/", status_code=status.HTTP_201_CREATED)
async def course(course_data:CourseCreate,db: AsyncSession = Depends(get_db)):
    """
        Write Operation: Creates a new course record in Neon.
    """
    new_course = CourseDB(course_code = course_data.course_code,
                             title=course_data.title,
                             description=course_data.description,
                             credits=course_data.credits )
    try:
            db.add(new_course)
            await db.flush() # Flushes data to database to trigger constraints/generate defaults
            return {"message": "course created successfully", "course_id": new_course.course_id}
    except Exception as e:
            # Handles cases like Duplicate Email errors cleanly
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Database operational failure: {str(e)}"
            )

@app.post("/enrollments/", status_code=status.HTTP_201_CREATED)
async def enroll_student(enrollment_data: EnrollmentCreate, db: AsyncSession = Depends(get_db)):
    """
    Write Operation: Enrolls a student into a course for a specific semester.
    """
    new_enrollment = EnrollmentDB(
        student_id=str(enrollment_data.student_id),
        course_id=str(enrollment_data.course_id),
        semester=enrollment_data.semester
    )
    
    try:
        db.add(new_enrollment)
        await db.flush()
        return {"message": "Enrollment recorded successfully", "enrollment_id": new_enrollment.enrollment_id}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Enrollment failed. Student may already be registered for this course this semester."
        )