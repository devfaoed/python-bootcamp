my_list = [1, 2, 3]

# traditional function
def add_to_list(item):
    return my_list.append(item)

add_to_list(4)

print(my_list)


# pure fufnction
def add_pureunc(item):
    my_list.append(item)
    return my_list

new_list = add_pureunc(5)
print(new_list)