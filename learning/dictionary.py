wordWorld = {1:"adedokun", 2:"faith", 3:"elijah", 4:"oluwatosin"}
print(wordWorld)

# accessing a value in a dectionary using a key
print(wordWorld[2]) 

# removing a value in a dectionary using a key
del wordWorld[4]
print(wordWorld)


# yet another dictionary
myDB =  {"age": 20}
print(type(myDB))
print(myDB["age"])

# adding a new item into a dictionary
myDB["favorites"] = "sleeping"
print(myDB)

# looping a dictinary
# first set
for x in wordWorld:
    print(x)

# another set
for key, value in wordWorld.items():
    print(str(key)  + " : " + value)

for key, value in myDB.items():
    print(str(key) + " = " + str(value))