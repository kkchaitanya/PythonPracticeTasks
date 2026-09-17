from typing import Optional
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel, EmailStr, Field
import uvicorn


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
@app.get("/courses")
def get_course():
    return courses_db

# 4. GET Endpoint to fetch a course by ID
# @app.get("/courses/")
# def get_category(category: str):
#    filter_cat = {
#     cat_id: item 
#     for cat_id, item in courses_db.items() 
#     if item.category.lower() == category.lower()
#             }
#    return filter_cat

# @app.get("/courses/")
# def get_category(category:Optional[str] = None,active: Optional[bool]=None):
# #    filter_cat = {
# #     cat_id: item 
# #     for cat_id, item in courses_db.items() 
# #         item.category.lower() == category.lower()
# #             }
#    filtered_courses = {}
#    for cat_id, item in courses_db.items():
#         # Check category match if category parameter is provided
#         match_cat = (category is None) or (item.category.lower() == category.lower())
#         # Check active status match if active parameter is provided
#         match_active = (active is None) or (item.active_status == active)
#         print(match_cat)
#         print(match_active)
#         if match_cat and match_active:
#             filtered_courses[cat_id] = item
#    return filtered_courses

@app.get("/courses/")
def get_courses(
    category: Optional[str] = None, 
    active: Optional[bool] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    filtered_courses = {}
    
    for cat_id, item in courses_db.items():
        # 1. Category Filter
        if category and item.category.lower() != category.lower():
            continue
            
        # 2. Active Status Filter
        if active is not None and item.active_status != active:
            continue
            
        # 3. Minimum Price Filter
        if min_price is not None and item.price < min_price:
            continue
            
        # 4. Maximum Price Filter
        if max_price is not None and item.price > max_price:
            continue
            
        # If the item passes all active checks, add it to the results
        filtered_courses[cat_id] = item
            
    return filtered_courses

@app.get("/active_courses/")
def get_course(active: bool):
   filter_cat = {
    cat_id: item 
    for cat_id, item in courses_db.items() 
    if item.active_status == active
            }
   return filter_cat
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)