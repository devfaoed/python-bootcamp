class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
    
class supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class chef(Employees):
    def leave_request(self, days):
        return "can i take leave for " + str(days) + " days"
    
Tosin =  supervisor("Adedokun", "A", "Faith")
Victor =  chef("Victor", "V")
Zazzu =  chef("Portable", "P")

print(Victor.leave_request(100))
print(Tosin.password)
print(Victor.name)