# ---------------------------------------------------------
# 4. FASTAPI APP & WRITE OPERATIONS
# ---------------------------------------------------------
from datetime import datetime
from bson import ObjectId
from fastapi import FastAPI, HTTPException,status
from databe import *
from models import TicketCreate, TicketStatus

app = FastAPI(title=" MongoDB-Based Support Ticket API")

@app.post("/create_ticket/", status_code=status.HTTP_201_CREATED)
async def create_ticket(ticketCreate: TicketCreate):
    try:
        ## convert class to JSON 
        ticket_doc = ticketCreate.model_dump() 
        ticket_doc["status"] = TicketStatus.OPEN
        ticket_doc["created_at"] = datetime.utcnow()
        ticket_doc["updated_at"] = datetime.utcnow()
        result = await ticket_collection.insert_one(ticket_doc)
        return {
            "message": "Ticket created successfully",
            "ticket_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}"
        )
    
@app.get("/tickets")
async def get_tickets():
    tickets = await ticket_collection.find().to_list(length=None)
    for ticket in tickets:
        ticket["_id"] = str(ticket["_id"])
    return tickets

@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: str):
    ticket = await ticket_collection.find_one(
        {"_id": ObjectId(ticket_id)}
    )
    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    ticket["_id"] = str(ticket["_id"])
    return ticket

@app.get("/tickets_by_status_priority")
async def get_tickets(status: str | None = None,priority: str | None = None):
    query={}
    if(status):
        query["status"] =status
    if(priority):
        query["priority"]= priority
    tickets = await ticket_collection.find(query).to_list(length=None)
    for ticket in tickets:
        ticket["_id"] = str(ticket["_id"])
    return tickets