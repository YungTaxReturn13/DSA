# This code demonstrates that Python Lists use a dynamic array for it's implementation.
# We can see that the list uses up extra memory to have additional spaces at the end of the list and increases
# as we continue to add items in chunks

# It is worth noting that because a list is a referential structure, the result of getsizeof for a list instance
# only includes the size for representing its primary strcuture; it does not account for the memeory used by the
#  objects in the list

import sys  # Provides the getsizeof function

data = []  # initializes our list
n = 30  # the number of iterations we would like to see

for i in range(n):
    a = len(data)  # number of elements in our list
    b = sys.getsizeof(data)  # the actual size in bytes that our lists takes up
    print(f"Length: {a}; Size in bytes: {b}")
    data.append(None)
