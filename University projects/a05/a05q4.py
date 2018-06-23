import check

# is_folded(old, new) returns if the new strand can be folded from the old 
# strand by removing either the first or last of the old and adding to the 
# end of the new
# is_folded: Str Str -> Bool
# requires: len(old) == len(new)
# Example: is_folded('AACTC', 'ACATC') => True

def is_folded(old, new):
    if old == '':
        return True
    elif old[0] == new[0]:
        return True and is_folded(old[1:], new[1:])
    elif old[-1] == new[0]:
        return True and is_folded(old[:-1], new[1:])
    else:
        return False
    
# Tests:
check.expect('Q4T1', is_folded('A', 'A'), True)
check.expect('Q4T2', is_folded('C', 'A'), False)
check.expect('Q4T3', is_folded('', ''), True)
check.expect('Q4T4', is_folded('AC', 'CA'), True)
check.expect('Q4T5', is_folded('AC', 'AC'), True)