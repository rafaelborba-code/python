def isPalindrome(self, x: int) -> bool:
    invertido = str(x)[::-1]
    if x == invertido:
        return True
    else:
        return False