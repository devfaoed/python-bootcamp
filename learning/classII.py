class recipe:
    def __init__(self, dish, items, times) -> None:
        self.items = items
        self.dish = dish
        self.times = times

    def contents(self):
        print("The " + str(self.dish) + " has " + str(self.items) + \
              " and takes " + str(self.times) + " to be prepared")
        

pizza = recipe("Pizza", ["chess", "bread", "tomato"], 45)
rice = recipe("Rice", ["rice", "papper", "oil", "maggi"], 45)

print(pizza.items)
print(rice.items)


print(pizza.contents())
print(rice.contents())


# another example
# Define class MyFirstClass
class MyFirstClass:
    # Define string variable called index
    index  = "Author-Book"
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        print( philosopher + " wrote the book: " + book)
        pass
        
# Call function handlist()
whodunnit = MyFirstClass()
print(whodunnit.hand_list("Sun Tzu", "The Art of War",))