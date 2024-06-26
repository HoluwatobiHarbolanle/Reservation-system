tables = [
    {'table': 1, 'seats': 6},
    {'table': 2, 'seats': 5},
    {'table': 3, 'seats': 4},
    {'table': 4, 'seats': 7},
    {'table': 5, 'seats': 3},
    {'table': 6, 'seats': 7},
]

def view_tables(tables):
    for table in tables:
        print(table)
view_tables(tables)

reservations = {}

def make_reservation(tables, reservations):
    #List requirement in reserving a table.
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    party_size = int(input("Enter the number of people: "))
    date = input("Enter date of event (YYY-MM-DD): ")
    start_time = input("Enter event start-time (HH:MM): ")
    end_time = input("Enter event end-time (HH:MM): ")

    #Write a function to get the available tables.
    available_tables = [table for table in tables if table['seats'] >= party_size and table['table'] not in reservations]
    if not available_tables:
        print("No available tables for your party size.")
        return
    print("Available tables: ")
    for table in available_tables:
        numbers = table['table']
        print(f"Table {table['table']} - Seats {table['seats']}")
        # print(numbers)
        #Make a reservation from the available tables.
        table_number = int(input("Enter the desired table number: "))
        if table_number != numbers:
            print("Invalid table number.")
            return

    # for i in table_numbers:
    reservation = {'name': name, 'party-size': party_size}
    print(f"The table {table_number} has been succesfully reserved for {name}.")

make_reservation(tables, reservations)
