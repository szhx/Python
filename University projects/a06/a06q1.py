import check
import math

# nat2bin(n) returns a list of 1 and 0 that represent number
# n in binary operation, the list is in decreasing power of 2s.
# nat2bin: Nat -> (listof (anyof 0 1))
# Example: nat2bin(12) => [1, 1, 0, 0]

def nat2bin(n):
    if n%2 == 0:
        a = 0
    else:
        a = 1
    n = n-a
    b = []
    while n > 0:    
        b = [int((n/2)%2)] + b
        n = int(n/2) - int((n/2)%2)
    return b+[a]  

# Tests:
check.expect('Q1AT1', nat2bin(5), [1,0,1])
check.expect('Q1AT2', nat2bin(2), [1,0])
check.expect('Q1AT3', nat2bin(1), [1])
check.expect('Q1AT4', nat2bin(0), [0])
check.expect('Q1AT5', nat2bin(3), [1,1])

# nat2base(n, base) returns the coverted value of n using the base 
# which the value is the increasing power of the base times a quotient
# and the most significant digit is at the beginning the unit digit at the end.
# nat2base: Nat Nat -> (listof Nat)
# requires: base >= 2
# Example: nat2base(12, 2) => [1, 1, 0, 0] 
def nat2base(n, base):
    if n%base < base:
        c = n%base
    else:
        c = 0
    n = n-c
    d =[]
    while n > 0:
        d = [int((n/base)%base)] + d
        n = int(n/base) - int((n/base)%base)
    return d+[c]
        
# Tests:
check.expect('Q1BT1', nat2base(245, 10), [2, 4, 5])
check.expect('Q1BT2', nat2base(326, 5), [2, 3, 0, 1])
check.expect('Q1BT3', nat2base(165, 16), [10, 5])
check.expect('Q1BT4', nat2base(36, 36), [1, 0])
check.expect('Q1BT5', nat2base(35, 36), [35])
check.expect('Q1BT6', nat2base(0, 10), [0])