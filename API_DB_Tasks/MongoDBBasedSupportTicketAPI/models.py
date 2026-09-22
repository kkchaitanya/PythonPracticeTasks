from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class TicketStatus(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    
class TicketPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class TicketCategory(str, Enum):
    AUTHENTICATION = "Authentication"
    BILLING = "Billing"
    TECHNICAL = "Technical"
    FEATURE_REQUEST = "Feature Request"

class Customer(BaseModel):
    name: str
    email: EmailStr

class Comment(BaseModel):
    author: str
    message: str
    created_at: datetime

class TicketCreate(BaseModel):
    customer: Customer
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10)
    category: TicketCategory
    priority: TicketPriority
    # category: str
    # priority: str
    tags: List[str]
    comments: List[Comment]
    # created_at: datetime
    # updated_at: datetime
    # status:TicketStatus
    # status:str

class TicketUpdate(BaseModel):
    title: Optional[str] = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(..., min_length=10)
    category: Optional[TicketCategory]
    priority: Optional[TicketPriority]
    tags: Optional[List[str]]
