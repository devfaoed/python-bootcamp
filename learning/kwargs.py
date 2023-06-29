def sumValues(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum
    # return round(sum, 2)

print(sumValues(coffie = 26.99, cake = 5.24, milk = 4.99))