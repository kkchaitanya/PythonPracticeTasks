from enum import Enum


class Category(Enum):
    PAYMENT = "Payment"
    TECHNICAL = "Technical"
    LOGIN = "Login"
    COURSE = "Course"
    REFUND = "Refund"
    ACCOUNT = "Account"

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class Status(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class Ticket:
    def __init__(
        self,
        ticket_id,
        customer_name,
        category,
        priority,
        status,
        assigned_agent,
        resolution_time
    ):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.category = category
        self.priority = priority
        self.status = status
        self.assigned_agent = assigned_agent
        self.resolution_time = resolution_time

    def __repr__(self):
        return (
            f"Ticket("
            f"ticket_id={self.ticket_id}, "
            f"customer_name='{self.customer_name}', "
            f"category='{self.category.value}', "
            f"priority='{self.priority.value}', "
            f"status='{self.status.value}', "
            f"assigned_agent='{self.assigned_agent}', "
            f"resolution_time={self.resolution_time}"
            f")"
        )