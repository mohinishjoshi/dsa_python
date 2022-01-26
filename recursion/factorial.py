def factorial(n):
    assert 0 <= n == int(n), "Only positive integers are allowed!"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

# n = -1  # Will raise assert error
# n = 1.5 # Will raise assert error
n = 5
print(f"The factorial of {n} is {factorial(n)}")