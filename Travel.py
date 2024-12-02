from Money import Money

GAS_COST_CENTS = .67
SEVENTY_NINE_SEVENTY_FIVE = 1.8
SEVENTY_NINE_HUNDRED = 1.7

class Building:
    def __init__(self, building1, building2, tripType=1):
        self.building1 = building1
        self.building2 = building2
        self.tripType = tripType

    @property
    def miles(self):
        return miles(self.building1, self.building2)


    @property
    def cost(self) -> str:
        money = Money(self.miles*float(self.tripType)*GAS_COST_CENTS)
        return money.get_money()
    
    def __str__(self):
        return f"The building is from {self.building1} to {self.building2} and the trip type is {self.tripType}\nThe total miles is {self.miles} and the cost is ${self.cost}"

def miles(building1, building2):
    if(building1 == "7975" or building2 == "7975"):
        if(building1 == "7900" or building2 == "7900"):
            return 1
        elif building1 == "6625" or building2 == "6625":
            return SEVENTY_NINE_SEVENTY_FIVE
        else:
            return 0
    elif building1 == "7900" or building2 == "7900":
        if building1 == "6625" or building2 == "6625":
            return SEVENTY_NINE_HUNDRED
        else:
            return 0
    else:
        return 0
