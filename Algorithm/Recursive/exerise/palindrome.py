def is_palindrome(s):
    if len(s) == 0:
        raise ValueError("String is empty")
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
