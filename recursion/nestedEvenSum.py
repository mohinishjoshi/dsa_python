obj1 = {
    "a": 2,
    "b": {
        "c": 2,
        "d": {
            "e": 8,
            "f": 3,
            "g": "yup"
        }
    }
}


def nestedEvenSum(obj):
    final_sum = 0
    if obj is None:
        return final_sum
    for value in obj.values():
        if type(value) == int and value % 2 == 0:
            final_sum += value
        elif type(value) is dict:
            final_sum += nestedEvenSum(value)
    return final_sum


print(nestedEvenSum(obj1))
