import check

# bin2nat(bistr) returns the decimal value of the binary number in the/
# string
# bin2nat: Str -> Nat
# Example: bin2nat("101") => 5

def bin2nat(bistr):
    if len(bistr) == 0:
        return 0
    else:
        return int(bistr[0:1])*(2**(len(bistr)-1))+bin2nat(bistr[1:])

# Tests:
check.expect("Q2T1", bin2nat("1111"), 15)
check.expect("Q2T2", bin2nat("111"), 7)
check.expect("Q2T3", bin2nat("0"), 0)
check.expect("Q2T4", bin2nat("1"), 1)
check.expect("Q2T5", bin2nat("10"), 2)
check.expect("Q2T6", bin2nat("100"), 4)