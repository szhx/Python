import check

testdata = '+++--+++---+-++---'

# max_height(desc) returns the maximum height of the given desc that the 
# picture of the desc can be drew.
# max_height: Str -> Nat
# Example: max_height('+-') => 4

def max_height(desc):
    if desc == '':
        return 0
    if desc[-1] == '+':
        c = 1
    else:
        c = -1
    a = []
    b = 0    
    while len(desc) > 1:
        if desc[0] == '+':
            b = b+1
            a = a+[b]
            desc = desc[1:]
        else:
            b = b-1
            a = a+[b]
            desc = desc[1:]
    a = a+[b+c]
    return max(a)

# Tests:
check.expect('Q4AT1', max_height(testdata), 4)
check.expect('Q4AT2', max_height('+-'), 1)
check.expect('Q4AT3', max_height(''), 0)
check.expect('Q4AT4', max_height('-+'), 0)

