import check

# binary_search(L, target) returns the index if target is
# in L and False otherwise
# binary_search: (listof Int) Int -> Anyof Nat or Bool
# Example: binary_search([1, 3, 4], 3) => 1

def binary_search(L, target):
    beginning = 0
    end = len(L) - 1
    while beginning <= end:
        middle = beginning + (end - beginning) // 2
        if L[middle] == target:
            return middle
        elif L[middle] > target:
            end = middle - 1
        else:
            beginning = middle + 1
    return False

# galloping_search(n, L) returns the index of the number in the list that is
# equal to the required number.
# Effects: print galloping search on each line with the starting index
#          of the binary search between 2 index
# galloping_search: Int (listof Nat) -> Nat
# Example: galloping_seach(1, [1, 2, 3]) => 0

def galloping_search(n, L):
    ind = 0
    while ind < len(L):
        if L[ind] == n:
            print('Galloping search from index '+str(ind))
            return ind
        elif L[ind] < n:
            print('Galloping search from index '+str(ind))
            ind = 2*(ind+1)-1
            if ind >= len(L)-1:
                if L[len(L)-1] == n:
                    print('Galloping search from index '+str(len(L)-1))
                    return len(L)-1
                else:
                    print('Galloping search from index '+str(len(L)-1))
                    return False            
        else:
            print('Galloping search from index '+str(ind))
            L_new = L[int((ind+1)/2):ind]
            print('Binary search from index '+str(int((ind+1)/2))+' to '+str(ind-1))
            if binary_search(L_new, n) == False:
                return False
            else:
                return int((ind+1)/2)+binary_search(L_new, n)

# Tests:
check.set_screen('Galloping search from index 0\nGalloping search from index/1\nGalloping search from index 3\nGalloping search from index 7\nBinary search from index 4 to 6')
check.expect('Q3T1', galloping_search(14, [1, 2, 5, 7, 9, 14, 15, 23, 29]), 5)
check.set_screen('Galloping search from index 0\nGalloping search from index/1\nGalloping search from index 3')
check.expect('Q3T2', galloping_search(7, [1, 2, 5, 7, 9]) , 3)
check.set_screen('Galloping search from index 0\nGalloping search from index/1\nGalloping search from index 3\nBinary search from index 2 to 2')
check.expect('Q3T3', galloping_search(3, [1, 2, 5, 7, 9]), False)
check.set_screen('Galloping search from index 0\nGalloping search from index/1\nGalloping search from index 3\nGalloping search from index 7\nGalloping search from index 9')
check.expect('Q3T4', galloping_search(100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]), 9)
check.set_screen('Galloping search from index 0\nGalloping search from index/1\nGalloping search from index 3\nGalloping search from index 7\nGalloping search from index 9')
check.expect('Q3T5', galloping_search(99, [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]), False)