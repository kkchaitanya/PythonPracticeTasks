from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import *
from models import *
from services import *
app = FastAPI(title="SQL Task Project API")

@app.post("/project/", status_code=status.HTTP_201_CREATED)
async def create_peoject(projectCreate: ProjectCreate, db: AsyncSession = Depends(get_db)):
    try:
        project_create = await create_project(db,projectCreate)
        return {"message": "Project created successfully", "project_id": project_create.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}")

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
async def create_tasks(projectCreate: TaskCreate, db: AsyncSession = Depends(get_db)):
   
    try:
        task_create = await create_task(db,projectCreate)
        return {"message": "Task created successfully", "task_create": task_create.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}")

@app.get("/tasks/")
async def cget_tasks(status:str=None,priority:Priority=None,assinged_to:str=None, db: AsyncSession = Depends(get_db)):
   
    try:
        fileted_data = await filter(db,status,priority,assinged_to)
        return {
         "result":   fileted_data
        }
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}")
