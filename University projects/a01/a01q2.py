import check

# fibonacci(n) returns an integer on nth position of the Fibonacci sequence
# by using a closed formula
# fibonacci: Nat -> Int
# requires: n<=70
# Examples: fibonacci(8) =>21

def fibonacci(n):
    fi = (1+(5**(1/2)))/2
    F = (fi**n-(-1/fi)**n)/(5**(1/2))
    Fn = int(F)
    return Fn

# Tests:
check.expect("Q2T1", fibonacci(1), 1)
check.expect("Q2T2", fibonacci(14), 377)
check.expect("Q2T1", fibonacci(70), 190392490709135)