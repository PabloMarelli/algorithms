
def maximumnumber(arr):
    if arr == []:
        return None
    if arr[0] > maximumnumber(arr[1:]):
        return arr[0]
    else:
        maximumnumber(arr[1:])

print(maximumnumber([1,2,5,8,9,22,4,3]))
