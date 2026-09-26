from datetime import datetime
from bson import ObjectId
from fastapi import FastAPI, HTTPException,status
from databe import *
from models import *

app = FastAPI(title="Project Ticket API")
@app.post("/create_project/", status_code=status.HTTP_201_CREATED)
async def create_project(projectCreate: ProjectCreate):
    try:
        ## convert class to JSON 
        project_create = projectCreate.model_dump() 
        project_create["created_at"] = datetime.utcnow()
        project_create["updated_at"] = datetime.utcnow()
        result = await project.insert_one(project_create)
        return {
            "message": "Project created successfully",
            "project_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}"
        )
    
@app.get("/projects")
async def get_projects():
    projects_list = await project.find().to_list(length=None)
    for prj in projects_list:
        prj["_id"] = str(prj["_id"])
    return projects_list

@app.post("/create_task/", status_code=status.HTTP_201_CREATED)
async def create_task(taskCreate: TaskCreate):
    try:
        project_inf = await project.find_one(
                {"_id": ObjectId(taskCreate.project_id)}
            )
        if not project_inf:
                raise HTTPException(
                    status_code=404,
                    detail="project not found"
                )
        ## convert class to JSON 
        task_create = taskCreate.model_dump() 
        task_create["status"]= TaskStatus.OPEN
        task_create["created_at"] = datetime.utcnow()
        task_create["updated_at"] = datetime.utcnow()
        result = await tasks.insert_one(task_create)
        return {
            "message": "task created successfully",
            "task_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}"
        )
@app.patch('/update_status/')
async def update_status(taskid: str, status:TaskStatus):
    try:
        task_id = await tasks.find_one(
                {"_id": ObjectId(taskid)}
            )
        if not task_id:
                raise HTTPException(
                    status_code=404,
                    detail="project not found"
                )  
        task_id["status"]= status
        task_id["updated_at"] = datetime.utcnow()
        result = await tasks.update_one(
                        {"_id": ObjectId(taskid)},
                        {"$set": task_id}
                        )
        if result.matched_count == 0:
                    raise HTTPException(
                    status_code=404,
                    detail="Ticket not found"
                    )
        return {
                "message": "Task Status Updated successfully"
                }
    except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Database operational failure: {str(e)}"
            )  
@app.get("/get_task/")
async def get_task(status:TaskStatus=None):
    try:
        query = {}
        if status:
            query["status"] = status
        cursor = tasks.find(query)
        tasks_list = await cursor.to_list()
        for prj in tasks_list:
                prj["_id"] = str(prj["_id"])
        return tasks_list
    except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Database operational failure: {str(e)}"
            )