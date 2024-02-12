from fastapi import APIRouter, HTTPException, Query
from schemas import TicketRequest
from database import context_aware_session
from models import Ticket
from test import getTickets, save_tickets_to_db

app = APIRouter()

@app.post("/generate_and_save_tickets/", response_model=dict)
async def generate_and_save_tickets(ticket_request: TicketRequest):
    try:
        tickets_dict = {}
        for idx in range(ticket_request.number_of_tickets):
            ticket_numbers = getTickets()
            tickets_dict[str(idx + 1)] = ticket_numbers

        formatted_tickets = {}
        for key, value in tickets_dict.items():
            formatted_tickets[key] = [str(sublist).replace(', ', ',') for sublist in value]

        formatted_response = {"tickets": formatted_tickets}
        save_tickets_to_db(list(tickets_dict.values()))
        return formatted_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

    
@app.get("/get_tickets", response_model=dict)
async def get_ticket(page: int = Query(default=1, ge=1), page_size: int = Query(default=10, ge=1)):
    session = context_aware_session()
    try:
        tickets = session.query(Ticket).offset((page - 1) * page_size).limit(page_size).all()
        ticket_numbers = {f"{ticket.id}": [str(list(row)) for row in ticket.ticket_numbers] for ticket in tickets}
        return {"tickets": ticket_numbers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

