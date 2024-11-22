from Travel import Building
from Data_Init import initialize_db
from Data_Man import create_entry, get_current_data

def user():
    prompt = ""
    while(prompt != "input" | "print"):
        prompt = input("Would you like to 'input' or 'print' data? Once data is printed it will be archived.")
    check_prompt(prompt)
    
    #return Building(convertLoc(location), travel)

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
        print_data()

def input_data():
    location = input("Enter '1' for 7975 and '2' for 7900: ")
    travel = input("Enter '1' for one way and '2' for roundtrip: ")
    building = Building(convert_loc(location), travel)
    create_entry(building)
    return f"Data has been added to storage!\n{building}"

def print_data():
    data = get_current_data()

def main():
    initialize_db
    print(user())

if __name__ == "__main__":
    main()