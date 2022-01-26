def get_binary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * get_binary(int(n/2))


for i in range(11):
    print(f"{i}:", get_binary(i))
