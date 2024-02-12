from pydantic import BaseModel
from typing import List
from enum import Enum

class TicketRequest(BaseModel):
    number_of_tickets: int

class TicketResponse(BaseModel):
    ticket_numbers: List[List[int]] 