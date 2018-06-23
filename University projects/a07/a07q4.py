import check
import math

# merge(L1, L2) returns a list of natural numbers that are in increasing 
# order that contains all elements from the given 2 lists which are already
# sorted in increasing order.
# merge: (listof Nat) (listof Nat) -> (listof Nat)
# Example: merge([1, 5], [2, 4]) => [1, 2, 4, 5]

def merge(L1,L2): 
    L = L1 + L2
    pos1,pos2,posL = 0,0,0 
    while (pos1 < len(L1)) and (pos2 < len(L2)): 
        if L1[pos1] < L2[pos2]:
            L[posL] = L1[pos1]
            pos1 = pos1+1 
        else: 
            L[posL] = L2[pos2] 
            pos2 = pos2+1
        posL = posL+1
    while (pos1 < len(L1)): 
        L[posL] = L1[pos1] 
        pos1, posL = pos1+1, posL+1
    while (pos2 < len(L2)):
        L[posL] = L2[pos2] 
        pos2, posL = pos2+1, posL+1
    return L

# merge3(L1, L2, L3) returns a list contains all elements from L1, L2 and L3
# and the list is in increasing order
# merge3: (listof Nat) (listof Nat) (listof Nat) -> (listof Nat)
# requires: L1, L2 and L3 are in increasing order
# Example: merge3([1, 5], [2, 7], [3, 4, 9]) => [1, 2, 3, 4, 5, 7, 9] 

def merge3(L1, L2, L3):
    L4 = merge(L1, L2)
    return merge(L4, L3)

# Tests:
check.expect('Q4AT1', merge3([], [], []), [])
check.expect('Q4AT2', merge3([1], [2], []), [1, 2])
check.expect('Q4AT3', merge3([2, 3], [5, 9], [2, 4]), [2, 2, 3, 4, 5, 9])
check.expect('Q4AT4', merge3([3, 6], [1, 2], [3, 5]), [1, 2, 3, 3, 5, 6])
check.expect('Q4AT5', merge3([2, 2], [2, 2], [2, 2]), [2, 2, 2, 2, 2, 2])

# mergesort3(L) returns a list with increasing elements in it by sorting the
# original list using merge sort method
# mergesort3: (listof Int) -> (listof Int)
# Example: mergesort3([2, 6, 1, 9, 3]) => [1, 2, 3, 6, 9]

def mergesort3(L):
    if L == []:
        return []
    if len(L) == 1:
        return L
    elif len(L) == 2:
        return merge3([L[0]], [L[1]], [])
    n = math.ceil(len(L) / 3)
    L1 = L[:n]
    L2 = L[n:n*2]
    L3 = L[n*2:]
    mergesort3(L1)
    mergesort3(L2)
    mergesort3(L3)
    return merge3(mergesort3(L1), mergesort3(L2), mergesort3(L3))
    
# Tests:
check.expect('Q4BT1', mergesort3([]), [])
check.expect('Q4BT2', mergesort3([1, 3, 7, 9]), [1, 3, 7, 9])
check.expect('Q4BT3', mergesort3([6, 3, 5, 1, 6, 9]), [1, 3, 5, 6, 6, 9])
check.expect('Q4BT4', mergesort3([3, 2, 5, 8, 2, 7, 4, 1]),
             [1, 2, 2, 3, 4, 5, 7, 8])
