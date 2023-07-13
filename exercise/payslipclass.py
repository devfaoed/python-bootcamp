class paySlip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    
    def pay(self):
        # self.payment = "yes"
        self.payment = True

    def status(self):
        # if self.payment == "yes":
        #     return self.name + " is paid" + str(self.amount)
        # else:
        #     return self.name + "has not paid yet"
        
        if self.payment:
            return self.name + " has paid " + str(self.amount)
        else:
            return self.name + " has not paid yet"

elijah = paySlip("elijah", False, 2000)
faith = paySlip("faith", False, " - ")

# status before payment
print(elijah.status(), "\n",  faith.status())



print("===========status ater payment========")
elijah.pay()
print(elijah.status(), "\n",  faith.status())

