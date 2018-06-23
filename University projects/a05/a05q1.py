import check

# helper1(A, B, a) returns the a with updated value by adding the products/
# of the number with the same index
# helper1: (listof Float) (listof Float) Nat -> Float
# requires: len(A) == len(B)
# Examples: helper1([-1.0, 2.0], [2.0, 1.0], 0.0) => 0.0

def helper1(A, B, a):
    if A == []:
        return a
    else:
        a = a + A[0] * B[0]
        return helper1(A[1:], B[1:], a)

# dot_product(A, B) returns the sum of the products of the number in 2 lists 
# with the same index
# dot_product: (listof Float) (listof Float) -> Float
# requires: len(A) == len(B)
# Examples: dot_product([-1.0, 2.0], [2.0, 1.0]) => 0.0

def dot_product(A, B):
    return helper1(A, B, 0)

# Tests:
check.within('Q1aT1', dot_product([0.0], [0.0]), 0.0, 0.001)
check.within('Q1aT2', dot_product([0.5, 2.0], [1.0, 0.0]), 0.5, 0.001)

# helper2(L, b) returns a list of poitive integers
# helper2: (listof Int) (listof Int) -> (listof Nat)
# effects: non_positive digits are eliminated
# Examples: helper2([1, 2, 6], []) => [1, 2, 6]

def helper2(L, b):
    if L == []:
        return b
    elif L[0] > 0:
        b = b + [L[0]]
        return helper2(L[1:], b)
    else:
        return helper2(L[1:], b)

# keep_postive(L) returns a filtered list with all the non_positive letters
# are eliminated
# keep_positive: (listof Int) -> (listof Nat)
# Examples:
# keep_positive([1,2,5]) => [1,2,5]

def keep_positive(L):
    return helper2(L, [])

# Tests:
check.expect('Q1bT1', keep_positive([0]), [])
check.expect('Q1bT2', keep_positive([1]), [1])
check.expect('Q1bT3', keep_positive([-5]), [])