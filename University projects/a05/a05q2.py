import check

# track_all(s, x) returns how many characters x in string s
# track_all: Str Str -> Nat
# Example:
# track_all('xxx', 'x') => 3

def track_all(s, x):
    if s == '':
        return 0
    elif x == s[0]:
        return 1 + track_all(s[1:], x)
    else:
        return track_all(s[1:], x)

# count_digits_acc(n, a, b) returns a list of number of characters from/
# a to 10 in n
# count_digits_acc: Str Nat (listof Nat) -> (listof Nat)
# effect: add a list to the original list b
# Example:
# count_digits_acc('123', 1, [2,3]) => [2,3,1,1,1,0,0,0,0,0,0]

def count_digits_acc(n, a, b):
    if a == 10:
        return b
    else:
        b = b + [track_all(n, str(a))]
        return count_digits_acc(n, a+1, b)

# count_digits(n) returns the number of digits from 0 to 9 in the number n
# count_digits: Nat -> (listof Nat)
# requires: n >= 0
# Example: 
# count_digits(345) => [0,0,0,1,1,1,0,0,0,0]

def count_digits(n):
    return count_digits_acc(str(n), 0, [])

# Tests:
check.expect('Q2T1', count_digits(1234567890), [1,1,1,1,1,1,1,1,1,1])
check.expect('Q2T2', count_digits(222), [0,0,3,0,0,0,0,0,0,0])