
def arraycount(arr):
    if arr == []:
        return 0
    return 1 + arraycount(arr[1:])

print(arraycount([1,2,3,4,5,6,7,8]))
