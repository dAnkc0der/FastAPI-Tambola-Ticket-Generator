import random
import numpy as np
from database import *
from models import Ticket


def getTickets():
    ticket_array = np.zeros((3, 9), dtype=int)
    total_numbers = [num for num in range(1, 90)]
    total_indices = [(i, j) for i in range(3) for j in range(9)]
    random_indices = []

    first_row = random.sample(total_indices[:9], 5)
    second_row = random.sample(total_indices[9:18], 5)
    third_row = random.sample(total_indices[-9:], 5)

    for i in first_row:
        random_indices.append(i)

    for i in second_row:
        random_indices.append(i)

    for i in third_row:
        random_indices.append(i)

    for num in random_indices:
        if num[1] == 0:
            number = random.choice(total_numbers[:10])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 1:
            number = random.choice(total_numbers[10:20])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 2:
            number = random.choice(total_numbers[20:30])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 3:
            number = random.choice(total_numbers[30:40])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 4:
            number = random.choice(total_numbers[40:50])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 5:
            number = random.choice(total_numbers[50:60])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 6:
            number = random.choice(total_numbers[60:70])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 7:
            number = random.choice(total_numbers[70:80])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 8:
            number = random.choice(total_numbers[80:89])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0

    for col in range(9):
        if(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            for row in range(2):
                if ticket_array[row][col] > ticket_array[row+1][col]:
                    temp = ticket_array[row][col]
                    ticket_array[row][col] = ticket_array[row+1][col]
                    ticket_array[row+1][col] = temp

        elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
            if ticket_array[0][col] > ticket_array[1][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[1][col]
                ticket_array[1][col] = temp

        elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
            if ticket_array[0][col] > ticket_array[2][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

        elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            if ticket_array[1][col] > ticket_array[2][col]:
                temp = ticket_array[1][col]
                ticket_array[1][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

    return ticket_array.tolist()


def save_tickets_to_db(tickets):
    db = SessionLocal()
    try:
        for ticket_numbers in tickets:
            ticket = Ticket(ticket_numbers=ticket_numbers)
            db.add(ticket)
        db.commit()
        db.refresh(ticket)
    finally:
        db.close()



