# learning about local scope
def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))




# learning  Enclosing scope

def get_totala(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    print(double)

    return total
# this scope will not return any output


#  Global scope
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total