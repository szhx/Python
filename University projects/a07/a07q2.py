import check

# count_longest_asc(L) returns the number of elements of a sublist obtained 
# from the original list that all elements in the sublist is in strictly
# increasing order.
# count_longest_asc: (listof Int) -> Nat
# Example: count_longest_asc([9, 1, 7, 8, 9, 4, 2]) => 4 

def count_longest_asc(L):
    if L == []:
        return 0
    ind = 1
    x = 1
    for i in range(len(L) - 1):
        if L[i] < L[i+1]:
            ind = ind + 1
        else:
            ind = ind + 0
        if x < ind:
            x = ind
    return x

# Tests:
check.expect('Q2T1', count_longest_asc([]), 0) 
check.expect('Q2T2', count_longest_asc([6, 4, 4, 2]), 1) 
check.expect('Q2T3', count_longest_asc([1, 2, 3, 4]), 4)
check.expect('Q2T4', count_longest_asc([2, 2, 2, 2]), 1)
check.expect('Q2T5', count_longest_asc([2, 5, 3, 3]), 2) 