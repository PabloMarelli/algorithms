"""
Binary search

O(log n)

Algorithm that takes a sorted list and an element as an input and returns the position of the element.
It takes log n steps to find the element.
It goes to the middle of the list and checks if the element is in the first one or not, and discard the first part and do it over again until it finds the element position.
"""
# Binary search is an algorithm; its input is a sorted list
# If an element youre looking for is in that list binary search returns the position
# where it is located, otherwise it returns null.
# It takes log n steps to find the element.
# For example: for a linear search of 64 items, it takes a simple linear search to find 
# the worse case item 64 steps, while for the binary search it takes log n = 64: 6 steps
# to find the item

def binary_search(search_list, item):
    low = 0
    high = len(search_list)-1

    while low <= high:
        mid = (low + high)
        guess = search_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
