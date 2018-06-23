import check

# find_primes(x) returns true if the number it evaluated is a prime number
# find_primes: Nat -> Bool
# requires: x > 0

def find_primes(x):
    return helper1(x, 2)

def helper1(x, y):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x == y:
        return True
    elif x / y == int(x / y):
        return False
    else:
        return helper1(x, y + 1)
    
# count_primes(start,end) returns the number of prime numbers 
# from the starting parameter to the ending parameter
# count_primes: Nat Nat -> Nat
# requires: 0< end < 500
#           start > 0
# Example: count_primes(1, 10) => 4
  
def count_primes(start, end):
    return helper2(start, end, 0)

def helper2(a, b, c):
    if a == b:
        if find_primes(b):
            return c + 1
        else:
            return c
    elif a > b:
        return 0
    else:
        if find_primes(a):
            return helper2(a + 1, b, c + 1)
        else:
            return helper2(a + 1, b, c)

# Tests:
check.expect("Q4T1", count_primes(1, 10), 4)
check.expect("Q4T2", count_primes(13, 10), 0)
check.expect("Q4T3", count_primes(20, 20), 0)
check.expect("Q4T4", count_primes(2, 2), 1)
check.expect("Q4T5", count_primes(2, 10), 4)
check.expect("Q4T5", count_primes(2, 11), 5)