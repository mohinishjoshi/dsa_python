def gcd(a, b):
    assert int(a) == a and int(b) == b, "Both numbers must be integers!"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = 98, 42
# a, b = 8, 12 = 4
print(f"The power of {a, b} is {gcd(a, b)}")
