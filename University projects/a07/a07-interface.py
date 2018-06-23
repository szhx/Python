## In each function, copy the function header to your own file.
## Your solution will replace "pass" in the body of the functions.

# Question 2
def count_longest_asc(L):
    pass

# Question 3
# Note: For *the binary_search function only* you can change
# the design recipe and implementation as required (you will need to)
# in order to adapt the function for your solution to Q3

# binary_search(L, target) returns True if target is
# in L and False otherwise
# binary_search: (listof Int) Int -> Bool
def binary_search(L, target):
    beginning = 0
    end = len(L) - 1
    while beginning <= end:
        middle = beginning + (end - beginning) // 2
        if L[middle] == target:
            return True
        elif L[middle] > target:
            end = middle - 1
        else:
            beginning = middle + 1
    return False

def galloping_search(n, L):
    pass

# Question 4 - part a
def merge3(L1, L2, L3):
    pass

# Question 4 - part b
def mergesort3(L):
    pass
