from Money import Money

GAS_COST_CENTS = .67
SEVENTY_NINE_SEVENTY_FIVE = 1.8
SEVENTY_NINE_HUNDRED = 1.7

class Building:
    def __init__(self, building, tripType):
        self.building = building
        self.tripType = tripType

    @property
    def miles(self):
        if(self.building == "7975"):
            return SEVENTY_NINE_SEVENTY_FIVE
        else:
            return SEVENTY_NINE_HUNDRED
    
    @property
    def cost(self) -> str:
        money = Money(self.miles*float(self.tripType)*GAS_COST_CENTS)
        return money.get_money()
    
    def __str__(self):
        return f"The building is {self.building} and the trip type is {self.tripType}\nThe total miles is {self.miles} and the cost is ${self.cost}"
    
