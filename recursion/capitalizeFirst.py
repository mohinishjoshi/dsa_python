def capitalizeFirst(arr):
    finalArr = []
    if len(arr) == 0:
        return finalArr
    finalArr.append(arr[0].title())
    finalArr.extend(capitalizeFirst(arr[1:]))
    return finalArr


print(capitalizeFirst(["abc", "def", "ghi"]))