from Travel import Building
from Data_Init import initialize_db
from Data_Man import create_entry, get_current_data
from Data_Print import print_data

def user():
    prompt = ""
    while prompt != "input" and prompt != "print":
        prompt = input("Would you like to 'input' or 'print' data?")
    check_prompt(prompt)

def convert_loc(input):
    if(input == "1"):
        return "7975"
    elif(input == "2"):
        return "7900"
    else:
        raise SystemExit("Error: Incorrect input received")
    
def check_prompt(prompt):
    if(prompt == "input"):
        input_data()
    elif(prompt == "print"):
        send_print()
    """elif prompt == "input custom":
        custom_input()"""

def input_data():
    location = input("Enter '1' for 7975 and '2' for 7900: ")
    travel = input("Enter '1' for one way and '2' for roundtrip: ")
    building = Building(convert_loc(location), travel)
    create_entry(building)
    print(f"Data has been added to storage!\n{building}")
"""
Custom locations to be implemented later
def custom_input():
    location1 = input("Enter where you traveled from: ")
    location2 = input("Enter where you traveled to: ")
    travel = input("Enter '1' for one way and '2' for roundtrip: ")
    building = Building(convert_loc(location), travel)
    create_entry(building)
    print(f"Data has been added to storage!\n{building}")
"""


def send_print():
    data = get_current_data()
    print_data(data)

def main():
    initialize_db
    user()

if __name__ == "__main__":
    main()