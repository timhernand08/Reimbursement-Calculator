class Money:
    def __init__ (self, amount:float = 0):
        self.amount = amount*100

    def get_money(self) -> float:
        return round(self.amount/100, 2)
    
    def __str__(self):
        amount = self.amount_cents/100
        return f"{amount:.2f}"