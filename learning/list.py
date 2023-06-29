list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
# removing from the list item using pop function
list1.pop(4)
print(list1)

list2 = ["A", "B", "C", "D"]
print(*list2)
# adding to the list item using insert function
list2.insert(len(list2), "E")

print(*list2)

list3 = ["hello", 2, "world", 4, "gorand", True, 10.25]
print(list3, sep=",")
# adding to the list item using extend function
list3.extend([9, 162, 804])
print(list3)
# removing from the list item using del function
del list3[1]
print(*list3)


list4 = ["am", 8, "ohh", 56, [6,7,4], "algorand", ]
print(list4[4])
# adding to the list item using append function
list4.append("solana")
print(list4)
# iterating list using for loop
for x in list4:
    print("value:", x)