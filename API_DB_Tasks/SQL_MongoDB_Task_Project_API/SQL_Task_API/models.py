from enum import Enum

from pydantic import BaseModel

class TaskStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    BLOCKED = "BLOCKED"

class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class ProjectCreate(BaseModel):
    name: str
    description: str
    
class TaskCreate(BaseModel):
    project_id: str
    title: str
    description: str
    priority: Priority
    assigned_to:str