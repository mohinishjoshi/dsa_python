def isEven(n):
    return n % 2 == 0


def arrAny(arr, callback):
    if len(arr) == 0:
        return False
    if callback(arr[0]):
        return True
    return arrAny(arr[1:], callback)


print(arrAny([1, 3], isEven))
