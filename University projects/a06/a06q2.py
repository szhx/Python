import check

# find_bigger(ints) returns the list that sort the list ints with all 
# the values that are bigger than the values came before it.
# find_bigger: (listof Int) -> (listof Int)
# Example: find_bigger([0, 4, 5, 4]) => [0, 4, 5] 

def find_bigger(ints):
    if ints == []:
        a = []
    else:
        a = [ints[0]]
    for x in range(1, len(ints)):
        if ints[x-1] < ints[x]:
            a = a+[ints[x]]
            x = x+1
        else:
            x = x+1
    return a

# Tests:
check.expect('Q2T1', find_bigger([1, 2, 4, 4]), [1, 2, 4])
check.expect('Q2T2', find_bigger([1, 2, 3]), [1, 2, 3])
check.expect('Q2T3', find_bigger([-2, -4, -4, -1]), [-2, -1])
check.expect('Q2T4', find_bigger([1]), [1])
check.expect('Q2T5', find_bigger([]), [])
check.expect('Q2T6', find_bigger([1, 5, 4, 6, 5]), [1, 5, 6])