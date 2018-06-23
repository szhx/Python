import check

# is_palidrome(s) returns if the given string s is in palidrome form
# is_palidrome: Str -> Bool
# Example: is_palindrome('aba') => True

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    while len(s) > 1:
        if s[0] == s[-1]:
            return True
        else:
            return False
        s = s[1:-1]

# Tests:
check.expect('Q3T1', is_palindrome(''), True)
check.expect('Q3T2', is_palindrome('a'), True)
check.expect('Q3T3', is_palindrome('aba'), True)
check.expect('Q3T4', is_palindrome('abc'), False)
check.expect('Q3T5', is_palindrome('abcba'), True)