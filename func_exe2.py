def palindrome(name):
    a=name[::-1]
    if(a==name):
        return True
    return False
print(palindrome("naman"))        