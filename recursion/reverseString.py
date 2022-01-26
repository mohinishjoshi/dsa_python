def reverseString(str):
    if len(str) <= 1:
        return str;
    else:
        return str[-1] + reverseString(str[:len(str)-1])


print(reverseString("Python"))