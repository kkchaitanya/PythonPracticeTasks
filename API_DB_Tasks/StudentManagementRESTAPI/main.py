from datetime import date
from typing import Annotated, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, Path, Query, status
from pydantic import BaseModel, ConfigDict, EmailStr, Field

app = FastAPI(
    title="Student Management API",
    description="In-memory CRUD API demonstrating HTTP methods, status codes, and parameter handling.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# 1. In-Memory Data Store
# ---------------------------------------------------------------------------
# Key: UUID (as string), Value: dict containing student attributes
students_db: dict[str, dict] = {}


# ---------------------------------------------------------------------------
# 2. Pydantic Schemas
# ---------------------------------------------------------------------------
class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, examples=["Ada"])
    last_name: str = Field(..., min_length=2, max_length=50, examples=["Lovelace"])
    email: EmailStr = Field(..., examples=["ada.lovelace@example.com"])
    date_of_birth: date = Field(..., examples=["2002-12-10"])
    department: str = Field(..., min_length=2, max_length=50, examples=["Computer Science"])
    gpa: float = Field(..., ge=0.0, le=4.0, examples=[3.85])


class StudentCreate(StudentBase):
    """Used for POST /students (Creation)."""
    pass


class StudentPut(StudentBase):
    """Used for PUT /students/{id} (Full replacement - all base fields required)."""
    pass


class StudentPatch(BaseModel):
    """
    Used for PATCH /students/{id} (Partial update).
    All fields are optional; only provided keys get applied.
    """
    first_name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    date_of_birth: Optional[date] = None
    department: Optional[str] = Field(None, min_length=2, max_length=50)
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)


class StudentResponse(StudentBase):
    """Serialized representation sent back to the client."""
    id: UUID

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------------------------------------------
# 3. Helper Functions
# ---------------------------------------------------------------------------
def ensure_unique_email(email: str, current_student_id: Optional[str] = None):
    for s_id, s_data in students_db.items():
        if s_data["email"].lower() == email.lower() and s_id != current_student_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"A student with email '{email}' already exists.",
            )


# ---------------------------------------------------------------------------
# 4. API Endpoints
# ---------------------------------------------------------------------------

# POST /students — Create student
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new student",
)
async def create_student(payload: StudentCreate):
    ensure_unique_email(payload.email)

    new_id = str(uuid4())
    student_record = payload.model_dump()
    student_record["id"] = UUID(new_id)

    students_db[new_id] = student_record
    return student_record


# GET /students — List students (with query params for filtering & pagination)
@app.get(
    "/students",
    response_model=list[StudentResponse],
    status_code=status.HTTP_200_OK,
    summary="List students",
)
async def list_students(
    department: Annotated[
        Optional[str],
        Query(description="Filter students by department (case-insensitive)"),
    ] = None,
    min_gpa: Annotated[
        Optional[float],
        Query(ge=0.0, le=4.0, description="Filter students with GPA greater than or equal to this value"),
    ] = None,
    skip: Annotated[int, Query(ge=0, description="Pagination offset")] = 0,
    limit: Annotated[int, Query(ge=1, le=100, description="Maximum number of items to return")] = 10,
):
    results = list(students_db.values())

    if department:
        results = [s for s in results if s["department"].lower() == department.lower()]

    if min_gpa is not None:
        results = [s for s in results if s["gpa"] >= min_gpa]

    return results[skip : skip + limit]


# GET /students/{id} — Get single student by path parameter
@app.get(
    "/students/{id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK,
    summary="Retrieve a student by ID",
)
async def get_student(
    id: Annotated[UUID, Path(description="The unique UUID of the student")],
):
    student_id_str = str(id)
    if student_id_str not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID '{id}' not found.",
        )
    return students_db[student_id_str]


# PUT /students/{id} — Replace student (Full update)
@app.put(
    "/students/{id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK,
    summary="Completely replace a student record",
)
async def replace_student(
    id: Annotated[UUID, Path(description="The unique UUID of the student")],
    payload: StudentPut,
):
    student_id_str = str(id)
    if student_id_str not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID '{id}' not found.",
        )

    # Validate that the new email doesn't collide with another student
    ensure_unique_email(payload.email, current_student_id=student_id_str)

    # Completely overwrite old data while keeping the same ID
    updated_record = payload.model_dump()
    updated_record["id"] = id
    students_db[student_id_str] = updated_record

    return updated_record


# PATCH /students/{id} — Partially update student
@app.patch(
    "/students/{id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK,
    summary="Partially update student attributes",
)
async def patch_student(
    id: Annotated[UUID, Path(description="The unique UUID of the student")],
    payload: StudentPatch,
):
    student_id_str = str(id)
    if student_id_str not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID '{id}' not found.",
        )

    # exclude_unset=True ignores fields the caller didn't pass in the request JSON
    update_data = payload.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request body must contain at least one field to update.",
        )

    if "email" in update_data:
        ensure_unique_email(update_data["email"], current_student_id=student_id_str)

    existing_record = students_db[student_id_str]
    existing_record.update(update_data)
    students_db[student_id_str] = existing_record

    return existing_record


# DELETE /students/{id} — Delete student
@app.delete(
    "/students/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a student",
)
async def delete_student(
    id: Annotated[UUID, Path(description="The unique UUID of the student")],
):
    student_id_str = str(id)
    if student_id_str not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID '{id}' not found.",
        )

    del students_db[student_id_str]
    # 204 No Content returns an empty body automatically
    return None