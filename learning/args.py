# using agruments do some mathematical calculations

# additions
def sumValues(*args):
    result = 0
    for x in args:
        result += x
    return result   

print(sumValues(5, 4, 10))

# multiplications
def mulValues(*args):
    total = 0
    for x in args:
        total -= x
    return total
print(mulValues(2, 6, 7, 8, 2, 10))