from models import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import *

async def create_project(db: AsyncSession,task_data: ProjectCreate):
    project_create= Project(name=task_data.name,
                            description=task_data.description)
    db.add(project_create)
    await db.flush()
    return project_create
async def create_task(db: AsyncSession,task_data: TaskCreate):
       task_create = Task(project_id=task_data.project_id,
                          title=task_data.title,
                          description = task_data.description,
                          priority = task_data.priority,
                          assigned_to=task_data.assigned_to)
       db.add(task_create)
       await db.flush()
       return task_create
async def filter(db: AsyncSession,status:str,priority:Priority,assinged_to:str):
       query = select(Task)

    #    if status:
    #     query = query.where(Task.status == status)
    #    if priority:
    #     query = query.where(Task.priority == priority)
    #    if assinged_to:
    #     query = query.where(Task.assigned_to == assinged_to)

       result = await db.execute(query)
       return result.scalars().all()