def devide_sum(a, b):
    return a / b

try:
    ans = devide_sum(40, 0)
    print(round(ans))
except Exception as e:
    print("Something wemt wrong with your input", e)