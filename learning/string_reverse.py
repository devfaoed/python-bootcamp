# how to reverse a string in python
# [start:stop:step]

#   Step 1
brand = "Dignity Technology"
reverseBrand = brand[::-1]
print(reverseBrand)
 

#  Step 2
def reverseMe(str):
    if len(str) == 0:
        return str
    else:
        return reverseMe(str[1:]) + str[0]

input = "Adedokun Faith Oluwatosin"
output = reverseMe(input)
print(output)