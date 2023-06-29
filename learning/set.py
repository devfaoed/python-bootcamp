set_a = {1, 2, 3, 4, 5, 10, 11, 13}

set_b = {1, 8, 6, 5, 7, 14, 15, 16}
print(set_a)
# to add an element into a set
set_a.add(6)
print(set_a)

# to remove an element from a set using remove() property
set_a.remove(2)
print(set_a)

# to remove an element from a set using discard() property
set_a.discard(4)
print(set_a)

# adding 2 set together using union property
print(set_a.union(set_b))

# adding 2 set together using or symbol
print(set_a | set_b)

# finding elements that exist between the 2 set
# using intersection method
print(set_a.intersection(set_b))

# using  and symbol
print(set_a & set_b)


# finding the diferrence between 2 sets
# using defference() property
print(set_a.difference(set_b))

# using - symbol
print(set_a - set_b)

# using symmetric_difference
print(set_a.symmetric_difference(set_b))

# symmetric_difference cab also be represented using ^
print(set_a ^ set_b)

## note 
# symmetric_difference will get all the total difference between 2 sets value

