def power(base, exp):
    assert 0 <= exp == int(exp), "Exponent should be a positive integer!"
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base, exp-1)


base, pow = 2.1, 5
print(f"The power of {base,pow} is {power(base,pow)}")