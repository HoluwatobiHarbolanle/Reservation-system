import csv
import os
tables = [
    {'table': 1, 'seats': 6},
    {'table': 2, 'seats': 5},
    {'table': 3, 'seats': 4},
    {'table': 4, 'seats': 7},
    {'table': 5, 'seats': 3},
    {'table': 6, 'seats': 7},
]


reservations_file = 'reservations_file.csv'

def view_tables(tables):
    for table in tables:
        print(table)
view_tables(tables)


def make_reservation(tables, reservations):
    #List requirement in reserving a table.
    name = input("Enter your name: ") #Prompt the user for their name.
    contact = input("Enter your contact number: ") #Prompt the user for their contact number.
    party_size = int(input("Enter the number of people: ")) #Enter the number of people to reseve for.
    date = input("Enter date of event (YYY-MM-DD): ") #Enter the date to reserve for.
    start_time = input("Enter event start-time (HH:MM): ") #Enter the start time of the event.
    end_time = input("Enter event end-time (HH:MM): ") #Enter the end time of the event.

    #Write a function to get the available tables.
    available_tables = [table for table in tables if table['seats'] >= party_size]
    if not available_tables:
    #If the condition to know the available tables is not true.
        print("No available tables for your party size.")
        return
    
    #Print out the available tables for user to know which to reserve.
    print("Available tables: ")
    for table in available_tables:
        print(f"Table: {table['table']} - Seats: {table['seats']}")

    #Make a reservation from the available tables.
    table_number = int(input("Enter the desired table number: "))
    if table_number not in [table['table'] for table in available_tables]:
        print("Invalid table number.")
        return
    
    #Create a list to store each reservation details.
    new_row = [table_number, name, contact, party_size, date, start_time, end_time]
    try:
        #Open the reservation file in an append mode.
        with open(reservations, mode='a', newline= '') as file:
            writer = csv.writer(file) #Create a writer object.
            writer.writerow(new_row) #Write in list in a row.
        #Print that a successful reservation is accomplished.
        print(f"The table {table_number} has been succesfully reserved for {name} on {date} starting from {start_time} to {end_time}.")
    except Exception as e:
        #Print an error message if there is any
        print(f"Error saving reservation: {e}")


make_reservation(tables, reservations_file)

def cancel_reservation(reservations):
    name_to_cancel = input("Enter the name of reservation to cancel: ") #Prompt the user for the name of reservation to cancel

    with open(reservations, mode= "r") as file: #Open the file in a read mode
        reader = csv.reader(file)
        reservationss = list(reader) #Save the reader object to a variable and change to list to allow modification since by default, it is now an iterator and can't be modified.

    for reservation in reservationss: #Loop through the lists.
        if reservation[1] == name_to_cancel: #Check if the name of the current reservation matches the user's input.
            del reservationss[reservationss.index(reservation)] #Identify the reservation with the index from the file content and delete.
            print(f"Reservation for name {name_to_cancel} has been successfully cancelled!")
            break #Break the loop afterwards.

    #Open the file again in a write mode.
    with open(reservations, mode="w", newline="") as file:
        writer = csv.writer(file) #Create the file object.
        writer.writerows(reservationss) # Write the updated list back into the file. If not written, the update will be temporary and the file will still retain it's original content.

cancel_reservation(reservations_file)

#Write another function to view the availability of tables.
def view_reservations(reservations):
    #Prompt users to input the date and start time.
    date = input("Enter the date (yy-mm-dd):") 
    time = input("Enter the start time (hh:mm):")
    with open(reservations, 'r') as file: #Open the file in a read mode.
        #Create a reader object and create a variable as it's placeholder.
        reader = csv.reader(file)
        reservations = list(reader)
    for i in reservations: #Loop through the reservations to check available date and time.
        if i[3] == date and i[4] == time:
            print(f"The date {date} and start time {time} has been taken.")
            break
        else :
            print(f"The date {date} and start time {time} are available.")
            break

view_reservations(reservations_file)