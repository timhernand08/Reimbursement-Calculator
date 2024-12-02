from Travel import Building
from Data_Man import create_entry, get_current_data
from Data_Print import print_data

    
def check_prompt(prompt):
    if(prompt == "input"):
        input_data()
    elif(prompt == "print"):
        send_print()
    """elif prompt == "input custom":
        custom_input()"""

def input_data(location1, location2, travel=1):
    building = Building(location1, location2, travel)
    create_entry(building)
    print(f"Data has been added to storage!\n{building}")

def send_print():
    data = get_current_data()
    print_data(data)