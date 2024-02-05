"""
Selection sort

O(n x n)

Algoritm to sort arrays or linked lists
To find the highest element you have to check every item in the list O(n) and you have to do this every n time. (one to select highest, remove that one, check all again, etc.)
"""

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr) 
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5,3,6,2,10]))
