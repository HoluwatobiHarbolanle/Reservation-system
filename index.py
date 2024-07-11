import csv
import datetime
# import os
tables = [
    {'table': 1, 'seats': 6},
    {'table': 2, 'seats': 5},
    {'table': 3, 'seats': 4},
    {'table': 4, 'seats': 7},
    {'table': 5, 'seats': 3},
    {'table': 6, 'seats': 7},
]

# reservations_file = 'reservations_file.csv'

def view_tables(tables):
    for table in tables:
        print(table)
view_tables(tables)

def make_reservation(tables, reservations):
    #List requirement in reserving a table.
    name = input("Enter your name: ").upper() #Prompt the user for their name.
    contact = input("Enter your contact number: ") #Prompt the user for their contact number.
    party_size = int(input("Enter the number of people: ")) #Enter the number of people to reseve for.
    date = input("Enter date of event (YYY-MM-DD): ") #Enter the date to reserve for.
    start_time = input("Enter event start-time (HH:MM): ") #Enter the start time of the event.
    end_time = input("Enter event end-time (HH:MM): ") #Enter the end time of the event.

    #Write a function to get the available tables.
    available_tables = [table for table in tables if table['seats'] >= party_size and str(table['table']) not in reservations]
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
            writer.writerow(new_row) #Write the list in a row.
        #Print that a successful reservation is accomplished.
        print(f"The table {table_number} has been succesfully reserved for {name} on {date} starting from {start_time} to {end_time}.")
    except Exception as e:
        #Print an error message if there is any
        print(f"Error saving reservation: {e}")

# make_reservation(tables, reservations_file)

def cancel_reservation(reservations):
    #Prompt the user for the details of table to cancel.
    table_number = input("Enter the number of table reservation to cancel: ")
    date = input("Enter the date reserved(YYYY-MM-DD): ")
    time = input("Enter the event start time(HH:MM): ")
    with open(reservations, mode= "r") as file: #Open the file in a read mode
        reader = csv.reader(file)
        reservations_content = list(reader) #Convert reader object to a list.

    for res in reservations_content:
        #Checking the matching value
        if res[0] == table_number and res[4] == date and res[5] == time:
            del reservations_content[reservations_content.index(res)]
#             # reservations_content.remove(reservation)
            print(f"Reservation for {res[1]} has been successfully cancelled!")
            break
    else :
        print("No matching reservation found.")
        
    #Open the file again in a write mode.
    with open(reservations, mode="w", newline="") as file:
        writer = csv.writer(file) #Create the file object.
        writer.writerows(reservations_content) # Write the updated list back into the file. If not written, the update will be temporary and the file will still retain it's original content.

#Write another function to view the reservations.
def view_reservations(reservations):
    with open(reservations, 'r') as file: #Open the file in a read mode.
        #Create a reader object and create a variable as it's placeholder.
        reader = csv.reader(file)
        header = next(reader)
        file_content = list(reader)
    for i in file_content: #Loop through the reservations to check available date and time.
        print(i)

#Function to modify a reservation details
def modify_reservation(tables, reservations):
    #Prompt user for details of reservation to modify
    name = input("Enter the name of reservation to modify: ").upper()
    table_number = input("Enter the number of table to modify: ").strip()
    date = input("Enter the date of reservation to modify(YYY_MM_DD): ").strip()
    #Open the file, create a reader object and get the header.
    with open(reservations, mode = "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        file_content = list(reader)
    #Loop through the file content and see if the condition passes, if not, return the function
    for i in file_content: 
        if i[header.index('Name')] == name and i[header.index('Table Number')] == table_number and i[header.index('Date')] == date:
            #Prompt the user for new details.
            New_name = input("Enter the new name for reservation: ").upper()
            New_contact = input("Enter your new contact number: ")
            New_party_size = int(input("Enter the new number of people: "))
            New_date = input("Enter new date of event (YYY-MM-DD): ")
            New_start_time = input("Enter event new start-time (HH:MM): ") 
            New_end_time = input("Enter event new end time: ")
            #Write a function to get the available tables.
            available_tables = [table for table in tables if table['seats'] >= New_party_size and str(table['table']) not in reservations]
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
            # while True:
            #Check if variables exists and replace it's value to the existing one.
            if New_name:
                i[header.index('Name')] = New_name
            if New_contact:
                i[header.index('Contact')] = New_contact
            if New_party_size:
                i[header.index('Party Size')] = New_party_size
            if New_date:
                i[header.index('Date')] = New_date
            if New_start_time:
                i[header.index('Start time')] = New_start_time
            if New_end_time:
                i[header.index('End time')] = New_end_time
                print(f"The reservation for {i[header.index('Name')]} has been modified.")
            break
    else:
        print("No matching details.")
        return
    #Open the file and rewrite in the updated content
    with open(reservations, mode="w", newline="") as file:
        writer = csv.writer(file) #Create the file object.
        writer.writerows(file_content)

#Function to view the reservations or reservation on a specified date.
def daily_summary(reservations):
    #Prompt user on the reservations to view
    date_type = int(input("Which summary will you like to view?\n1. Today\n2. Input date\n"))

    #Handle user's valueError if there is any
    try:
    #If user request for the current day reservations, get the date using datetime module
        if date_type == 1:
            date = datetime.date.today().strftime("%Y-%m-%d") #Convert to a string for comparison

    #If not, user should input the date of reservation to return.
        elif date_type == 2:
            date_str = input("Enter the date of reservation to return(YYYY-MM-DD): ")
            #Parse into a date object and convert to string for comparison sake.
            try:
                date = datetime.datetime.today().strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
            except:
                print("Invalid format. Please input date as this(YYYY-MM-DD)")
                return
        else :
            print("Invalid! Select an option from the available options.")
            return
    except ValueError:
        print("An integer is required.")
    #Open the file and create a reader object and get the header also.
    with open(reservations, mode= 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        reservations_file = list(reader)
    #Loop through and see if the condition passes
    for res in reservations_file:
        if res[header.index('Date')] == date:
            print(res)
            break
        else:
            print(f"No reservation found on this date {date}.")
            break

def options():
    print("\n1. Make reservation\n2. Cancel reservation\n3. View reservations\n4. Modify reservation\n5. View daily summary\n6. Exit")
    try:
        choice = int(input("Make a choice? "))
    except ValueError:
        print("An integer is required.")
        return
    while True:
        if choice == 1:
            make_reservation(tables, reservations_file)
        elif choice == 2:
            cancel_reservation(reservations_file)
        elif choice == 3:
            view_reservations(reservations_file)
        elif choice == 4:
            modify_reservation(tables, reservations_file)
        elif choice == 5:
            daily_summary(reservations_file)
        elif choice == 6:
            print("App exited!")
        else :
            print("Invalid choice! Try again.")
        break
# options()

#Implement the functions using class
class Reservation_system:
    __reservations_file = 'reservations_file.csv'
    def __init__(self):
        self._tables = tables
    @property
    def tables(self):
        return self._tables
    def view_tables(self,tables):
        for table in tables:
            print(table)
    def make_reservation(self):
        #List requirement in reserving a table.
        name = input("Enter your name: ").upper() #Prompt the user for their name.
        contact = input("Enter your contact number: ") #Prompt the user for their contact number.
        party_size = int(input("Enter the number of people: ")) #Enter the number of people to reseve for.
        date = input("Enter date of event (YYY-MM-DD): ") #Enter the date to reserve for.
        start_time = input("Enter event start-time (HH:MM): ") #Enter the start time of the event.
        end_time = input("Enter event end-time (HH:MM): ") #Enter the end time of the event.

        #Write a function to get the available tables.
        available_tables = [table for table in self._tables if table['seats'] >= party_size and str(table['table']) not in Reservation_system.__reservations_file]
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
            with open(Reservation_system.__reservations_file, mode='a', newline= '') as file:
                writer = csv.writer(file) #Create a writer object.
                writer.writerow(new_row) #Write the list in a row.
            #Print that a successful reservation is accomplished.
            print(f"The table {table_number} has been succesfully reserved for {name} on {date} starting from {start_time} to {end_time}.")
        except Exception as e:
            #Print an error message if there is any
            print(f"Error saving reservation: {e}") 
    def cancel_reservation(self, reservations):
        #Prompt the user for the details of table to cancel.
        table_number = input("Enter the number of table reservation to cancel: ")
        date = input("Enter the date reserved(YYYY-MM-DD): ")
        time = input("Enter the event start time(HH:MM): ")
        with open(reservations, mode= "r") as file: #Open the file in a read mode
            reader = csv.reader(file)
            reservations_content = list(reader) #Convert reader object to a list.

        for res in reservations_content:
            #Checking the matching value
            if res[0] == table_number and res[4] == date and res[5] == time:
                del reservations_content[reservations_content.index(res)]
#               # reservations_content.remove(reservation)
                print(f"Reservation for {res[1]} has been successfully cancelled!")
                break
        else :
            print("No matching reservation found.")
        
        #Open the file again in a write mode.
        with open(reservations, mode="w", newline="") as file:
            writer = csv.writer(file) #Create the file object.
            writer.writerows(reservations_content) # Write the updated list back into the file. If not written, the update will be temporary and the file will still retain it's original content.
    def view_reservations(self, reservations):
        with open(reservations, 'r') as file: #Open the file in a read mode.
            #Create a reader object and create a variable as it's placeholder.
            reader = csv.reader(file)
            header = next(reader)
            file_content = list(reader)
        for i in file_content: #Loop through the reservations to check available date and time.
            print(i)
    #Function to modify a reservation details
    def modify_reservation(self, tables, reservations):
        #Prompt user for details of reservation to modify
        name = input("Enter the name of reservation to modify: ").upper()
        table_number = input("Enter the number of table to modify: ").strip()
        date = input("Enter the date of reservation to modify(YYY_MM_DD): ").strip()
        #Open the file, create a reader object and get the header.
        with open(reservations, mode = "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            file_content = list(reader)
        #Loop through the file content and see if the condition passes, if not, return the function
        for i in file_content: 
            if i[header.index('Name')] == name and i[header.index('Table Number')] == table_number and i[header.index('Date')] == date:
                #Prompt the user for new details.
                New_name = input("Enter the new name for reservation: ").upper()
                New_contact = input("Enter your new contact number: ")
                New_party_size = int(input("Enter the new number of people: "))
                New_date = input("Enter new date of event (YYY-MM-DD): ")
                New_start_time = input("Enter event new start-time (HH:MM): ") 
                New_end_time = input("Enter event new end time: ")
                #Write a function to get the available tables.
                available_tables = [table for table in tables if table['seats'] >= New_party_size and str(table['table']) not in reservations]
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
                # while True:
                #Check if variables exists and replace it's value to the existing one.
                if New_name:
                    i[header.index('Name')] = New_name
                if New_contact:
                    i[header.index('Contact')] = New_contact
                if New_party_size:
                    i[header.index('Party Size')] = New_party_size
                if New_date:
                    i[header.index('Date')] = New_date
                if New_start_time:
                    i[header.index('Start time')] = New_start_time
                if New_end_time:
                    i[header.index('End time')] = New_end_time
                    print(f"The reservation for {i[header.index('Name')]} has been modified.")
                    break
        else:
            print("No matching details.")
            return
        #Open the file and rewrite in the updated content
        with open(reservations, mode="w", newline="") as file:
            writer = csv.writer(file) #Create the file object.
            writer.writerows(file_content)
    def daily_summary(self, reservations):
        #Prompt user on the reservations to view
        date_type = int(input("Which summary will you like to view?\n1. Today\n2. Input date\n"))

        #Handle user's valueError if there is any
        try:
        #If user request for the current day reservations, get the date using datetime module
            if date_type == 1:
                date = datetime.date.today().strftime("%Y-%m-%d") #Convert to a string for comparison

        #If not, user should input the date of reservation to return.
            elif date_type == 2:
                date_str = input("Enter the date of reservation to return(YYYY-MM-DD): ")
                #Parse into a date object and convert to string for comparison sake.
                try:
                    date = datetime.datetime.today().strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                except:
                    print("Invalid format. Please input date as this(YYYY-MM-DD)")
                    return
            else :
                print("Invalid! Select an option from the available options.")
                return
        except ValueError:
            print("An integer is required.")
        #Open the file and create a reader object and get the header also.
        with open(reservations, mode= 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations_file = list(reader)
        #Loop through and see if the condition passes
            for res in reservations_file:
                if res[header.index('Date')] == date:
                    print(res)
                    break
            else:
                print(f"No reservation found on this date {date}.")
                break
