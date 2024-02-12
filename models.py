from sqlalchemy import Column, Integer, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    ticket_numbers = Column(ARRAY(Integer, dimensions=2))

    