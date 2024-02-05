
def suma(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


print(suma([1,2,3,4]))


