menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    # Naive approach
    # subtotal = 0.0
    # for item in order:
    #     subtotal += item["price"]
    # return subtotal
    
    subtotal = round(sum(item.get("price", 0) for item in order), 2)
    return subtotal

def calculate_tax(subtotal):
    # Short approach
    # return round(subtotal * 0.15, 2)

    TAX_RATE = 0.15
    tax_amount = subtotal * TAX_RATE
    return round(tax_amount, 2)

def summarize_order(order):
    # Naive approach
    # subtotal = calculate_subtotal(order)
    # tax = calculate_tax(subtotal)
    # total = round(subtotal + tax, 2)
    # names = []
    # for item in order:
    #     names.append(item["name"])
    # return names, total
    
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item["name"] for item in order]
    return names, total

def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)
    
    print(f"Ordered items: {items}")
    print(f"Total sum of order: {subtotal}")

if __name__ == "__main__":
    main()
