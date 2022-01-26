def sumOfDigits(n):
    assert int(n) == n, "Number must be an integer!"
    if n == 0:
        return 0
    else:
        curr = n%10
        nxt = int(n / 10)
        return curr + sumOfDigits(nxt)


n = -12345
print(f"The sum of digits of {n} is {sumOfDigits(abs(n))}")