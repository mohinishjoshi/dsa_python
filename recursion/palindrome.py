def isPalindrome(str):
    if len(str) == 0:
        return True
    elif str[0] != str[-1]:
        return False
    return isPalindrome(str[1:-1])


print(isPalindrome("radar"))
print(isPalindrome("radidar"))
print(isPalindrome("raddir"))