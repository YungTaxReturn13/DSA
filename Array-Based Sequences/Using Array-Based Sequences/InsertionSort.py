"""Insertion sort starts with the first element in an array. Then considers the next element in the array, it it is smaller than the first, we swap them.
Next we consider the third element in the array and wap it lefward until it is in the proper order with the first two elements. 
We continue this until the whole array is sorted

The nested loops for insertion-sort lead to an O(n^2)"""

import random


def insertions_sort(A):
    """Sort list of comparable elements into nondecreasing order"""
    for i in range(1, len(A)):  # from 1 to n-1
        curr = A[i]  # current element to be possibly moved
        j = i  # variable used to find correct index for current
        while (
            j > 0 and A[j - 1] > curr
        ):  # goes back and checks previous elements that are less than curr
            A[j] = A[j - 1]  # moves the previous item up
            j -= 1  # decrements the index
        A[j] = curr  # once it breaks out of the loop, it has either
        # not moved, gone back to 0, or is in the correct position


x = random.sample(range(0, 100), 10)
print(x)
insertions_sort(x)
print(x)
