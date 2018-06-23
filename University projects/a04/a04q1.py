import check

# power_fn(n,k,t) returns the a list of natural number from the n's increasing
# power until k == 0
# power_fn: Nat Nat Nat -> listof (Nat)
# Example:  power_fn(2,4,0) => [1,2,4,8] 
def power_fn(n,k,t):
    if k == 0:
        return []
    else:
        return [n**t] + power_fn(n,k-1,t+1)

# powers(n,k) returns a list of natural number from n's increasing power from 0/
# to k-1
# powers: Nat Nat -> listof (Nat)
# Example: powers(2,4) => [1,2,4,8] 
def powers(n,k):
    return power_fn(n,k,0)

# Tests:
check.expect("Q1aT1", powers(1,0), [])
check.expect("Q1aT2", powers(1,1), [1])
check.expect("Q1aT3", powers(3,3), [1,3,9])

# count_wins(lst1,lst2) returns the number of times that the number in the /
# first list is larger than the number in the second list with the same index
# count_wins: listof (Nat) listof (Nat) -> Nat
# Require: 2 lists must in the same length
# Example: count_wins([1,2,0,4],[4,1,0,2]) => 2 
def count_wins(lst1,lst2):
    if lst1 == []:
        return 0
    elif lst1[0] > lst2[0]:
        return 1 + count_wins(lst1[1:],lst2[1:])
    else:
        return count_wins(lst1[1:],lst2[1:])

# Tests:
check.expect("Q1bT1", count_wins([],[]), 0)
check.expect("Q1bT2", count_wins([1],[2]), 0)
check.expect("Q1bT3", count_wins([2],[1]), 1)
check.expect("Q1bT4", count_wins([2],[2]), 0)
check.expect("Q1bT5", count_wins([2,1],[1,1]), 1)

# helper(lst1,lst2,a) returns nothing
# Effects: Mutate 2 lists by adding number in each index from a to the end
# helper: listof (Nat) listof (Nat) Nat -> None
# Example: add_lists([1,2,0],[1, 1, -1],0) => None 
def helper(lst1,lst2,a):
    if a == len(lst1):
        return None
    else:
        lst1[a] = lst1[a] + lst2[a]
        helper(lst1,lst2,a+1)

# add_lists(lst1,lst2) returns nothing 
# Effects: Mutate 2 lists by adding number in each index
# add_lists: listof (Nat) listof (Nat) -> None
# Example: add_lists([1,2,0],[1, 1, -1]) => None 
def add_lists(lst1,lst2):
    return helper(lst1,lst2,0)
    
# Tests:
L = [1,2,3]
G = [3,2,1]
check.expect("Q1cT1", add_lists(L,G), None)
check.expect("Q1cT1(L)", L, [4,4,4])