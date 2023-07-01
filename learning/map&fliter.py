# mapping through a list of item
menuList = ["rice jollof & fried", "rice salad", "yam", "potatoe", "amala", "chicken & Pasta", "semo", "pounded yam"]

# function to map through menulist and return its values
def orderFood(list):
    return list

foodItem = map(orderFood, menuList)
for item in foodItem:
    print(item)


# function to map thrrugh menulist and return values through a search input
def findFood(item):
    if item[0] == "r":
        return item
    
result = map(findFood, menuList)
print("================= map result ==========")
for list in result:
    print(list)

# filter
output = filter(findFood, menuList)
print("================= filter result ==========")
for item in output:
    print(item)

