import check

# calculator(n, a) returns the a mutated list which a '3n+1' sequence is/
# added to a
# calculator: Nat (list of Nat) -> (listof Nat)
# effect: add a new list of the original list
# requires: n <= 1000
# Example:
# calcultor(4, [2,3]) => [2,3,4,2,1] 

def calculator(n, a):
    if n == 1:
        return a + [1]
    elif n % 2 == 0:
        a = a + [n]
        n = n / 2
        return calculator(n, a)
    else:
        a = a + [n]
        n = 3 * n + 1
        return calculator(n, a)

# collatz_number(n) returns the length of a '3n+1' sequence
# collatz_number: Nat -> (listof Nat)
# requires: 0 <= n <= 1000
# Example:
# collatz_number(4) => 3

def collatz_number(n):
    return len(calculator(n, []))

# Tests:
check.expect('Q3T1', collatz_number(1), 1)
check.expect('Q3T2', collatz_number(5), 6)
check.expect('Q3T3', collatz_number(8), 4)
