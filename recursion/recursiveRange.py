def recursiveRange(n):
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n-1)


print(recursiveRange(5))
