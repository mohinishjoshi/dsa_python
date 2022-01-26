obj1 = {
    "a": "I'm here.",
    "b": {
        "c": 2,
        "d": {
            "e": "hello",
            "f": 3,
            "g": "yes"
        }
    }
}

def collectStrings(obj):
    collected = []
    if obj is None:
        return collected
    for val in obj.values():
        if type(val) is str:
            collected.append(val)
        if type(val) is dict:
            collected.extend(collectStrings(val))
    return collected

print(collectStrings(obj1))