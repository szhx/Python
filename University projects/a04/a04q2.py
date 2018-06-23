import check

# count_lowercase(lst1) returns the number of lowercase letters in a list
# count_lowercase: Str -> Nat
# Example:
# count_lowercase("HELLO World!") => 4
def count_lowercase(lst1):
    new1 = list(filter(lambda a: a[:1].isalpha(), lst1))
    return len(list(filter(lambda s: s[:1].islower(), new1)))

# count_uppercase(lst1) returns the number of capital letters in a list
# count_uppercase: Str -> Nat
# Example:
# count_uppercase("HELLO World!") => 6
def count_uppercase(lst2):
    new2 = list(filter(lambda a: a[:1].isalpha(), lst2))
    return len(list(filter(lambda t: t[:1].isupper(), new2)))

# shouting(s) returns the wether or not the sting contains more cpital letters/
# than lowercase letters
# shouting: Str -> Bool
# Example: shouting("HELLO World!") => True 
def shouting(s):
    if count_uppercase(s) > count_lowercase(s):
        return True
    else:
        return False

# Tests:
check.expect("Q2aT1", shouting(" "), False)
check.expect("Q2aT2", shouting("$@#$!"), False)
check.expect("Q2aT3", shouting("THIS IS gOOd"), True)
check.expect("Q2aT4", shouting("YES"), True)
check.expect("Q2aT5", shouting("no"), False)

# replace_match(a,b,c) returns the a new value (c) when a is equal to b
# replace_match: Int Int Int -> Int
# Example: replace_match(1,1,2) => 2
def replace_match(a,b,c):
    if a == b:
        return c
    else:
        return a

# replace(lst,match,rep) returns a list of integers with each number that is/
# the same as the match replaced by rep
# replace: listof (Int) Int Int -> listof (Int)
# Example: replace([1,2,-1,2], 2, 0) => [1,0,-1,0]
def replace(lst,match,rep):
    return list(map(lambda b: replace_match(b,match,rep), lst))

# Tests:
check.expect("Q2bT1", replace([], 2, 1), [])
check.expect("Q2bT2", replace([1,3,5], 2, 1), [1,3,5])
check.expect("Q2bT3", replace([1,3,2], 2, 1), [1,3,1])

# divisible(a,b) returns the quotient of a and b if their remainder is 0 or/ 
# return "*" otherwise
# divisible: Nat Nat -> Nat
# Example: divisible(2,2) => 1
def divisible(a,b):
    if a%b == 0:
        return a//b
    else:
        return "*"

# keep_quotients(lst,n) returns a list of quotients of elements with n that the/ 
# remainder is 0 
# keep_quotient: listof (Nat) Nat -> listof (Nat)
# Example: keep_quotient([6,8,7,2], 2) => [3,4,1]
def keep_quotients(lst,n):
    s = list(map(lambda c: divisible(c,n), lst))
    return list(filter(lambda d: not d=="*", s))

# Tests:
check.expect("Q2cT1", keep_quotients([], 1), [])
check.expect("Q2cT2", keep_quotients([2,3,5], 1), [2,3,5])
check.expect("Q2cT3", keep_quotients([5,3,1], 2), [])