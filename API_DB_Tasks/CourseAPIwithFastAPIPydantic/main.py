from typing import Optional
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel, EmailStr, Field


# 1. Initialize the FastAPI app
app = FastAPI(title="Course Management API")

# In-memory database simulation for testing
courses_db = {}
# 2. Define a Pydantic model for data validation
class Course(BaseModel):
     # Required field: Explicitly managed by the database/system in real apps, string here
    course_id: str = Field(..., description="Unique identifier for the course")
    # Validation: Minimum title length of 3 characters
    title: str = Field(..., min_length=3, description="The title of the course")
    # Required field
    description: str = Field(..., description="Detailed description of the course content")
    # Validation: Price must be strictly greater than 0
    price: float = Field(..., gt=0, description="Price of the course (must be greater than 0)")
    # Required field (e.g., "12 hours", "4 weeks")
    duration: str = Field(..., description="Duration of the course")
    # Required field
    instructor: str = Field(..., description="Name of the course instructor")
    # Required field (Categories can be open text, or restricted via Literal as shown below)
    category: str = Field(..., description="Genre or category of the course")
    # Validation: Ratings must fall between 0.0 and 5.0 (inclusive)
    rating: float = Field(..., ge=0.0, le=5.0, description="Course rating from 0.0 to 5.0")
    # Required field: Active status boolean
    active_status: bool = Field(..., description="Whether the course is currently active and available")


# 3. POST Endpoint to create a validated course
@app.post("/courses/", status_code=status.HTTP_201_CREATED, response_model=Course)
def create_course(course: Course):
    # Check if course ID already exists
    if course.course_id in courses_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Course with this ID already exists."
        )
    
    # Save to our in-memory database
    courses_db[course.course_id] = course
    return course

@app.put("/courses/", status_code=status.HTTP_202_ACCEPTED, response_model=Course)
def create_course(course: Course):
    # Check if course ID already exists
    if course.course_id not in courses_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Course with this ID already exists."
        )
    
    # Save to our in-memory database
    courses_db[course.course_id] = course
    return course

# 4. GET Endpoint to fetch a course by ID
@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: str):
    if course_id not in courses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Course not found."
        )
    return courses_db[course_id]

# 4. GET Endpoint to fetch a course by ID
@app.get("/courses/", response_model=Course)
def get_course(category: str):
    courses_db[courses_db["category"]]
    return courses_db[course_id]