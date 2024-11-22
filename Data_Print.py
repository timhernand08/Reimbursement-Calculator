from Money import Money
def print_data(data):
    print(f"{"Building":<15}{"Trip Type":<15}{"Miles":<15}{"Cost":<15}{"Date":<15}")
    total_cost:float  = 0
    for list in data:
        for index, variable in enumerate(list[1:6]):
            if index == 3:
                print(f"${variable:<15}", end="")
                total_cost += variable
            else:
                print(f"{variable:<15}", end="")
        print()
    print(f"Total to be reimbursed is ${total_cost:.2f}")
