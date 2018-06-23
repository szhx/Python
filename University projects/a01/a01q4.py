import check
import math

# reveal_secret(secret, fav_month, fav_day) returns the secret value after
# the specific calculation steps
# reveal_secret: Int Int Int -> Int
# requires: secret>2
#           fav_month is between 1 and 12
#           fav_day is between 1 and 31
# Examples: reveal_secret(101, 9, 12) => 101

def reveal_secret(secret, fav_month, fav_day):
    step1 = secret*3
    step2 = step1+secret-5
    step3 = step2*3*3
    step4 = step3+secret-fav_month
    step5 = step4*3*3*3
    step6 = step5+secret-fav_day
    step7 = step6//1000+2
    return step7

# Tests:
check.expect("Q4T1", reveal_secret(3, 1, 1), 3)
check.expect("Q4T2", reveal_secret(15, 12, 31), 15)
check.expect("Q4T3", reveal_secret(234, 4, 17), 234)