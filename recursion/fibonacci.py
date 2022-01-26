def fibonacci(n):
    assert 0 <= n == int(n), "Only positive integers are allowed!"
    if n in [0,1]:
        return n;
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 10
print(f"The fibonacci of {n} is {fibonacci(n)}")