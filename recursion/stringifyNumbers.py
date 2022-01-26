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


def stringifyNum(obj):
    newObj = {}
    if obj is None:
        return newObj
    for key in obj.keys():
        if type(obj[key]) in [int, float]:
            newObj[key] = str(obj[key])
        elif type(obj[key]) is dict:
            newObj[key] = stringifyNum(obj[key])
        else:
            newObj[key] = obj[key]

    return newObj


print(stringifyNum(obj1))
