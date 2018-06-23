import check

# basic_grade(assts, mid_exam, final_exam, clickers, tutorials) returns
# the total final grade in CS116 of the term with the percentage of each
# component are given
# basic_grade: Float Float Float Float Nat -> Int
# requires: assts, mid_exam, final_exam, clickers are between 0 and 100
#           tutorials are between 0 and 12 and the maximum added mark is 5
# Examples: basic_grade(60.0, 75.8, 90.0, 55.5, 9) => 79

def basic_grade(assts, mid_exam, final_exam, clickers, tutorials):
    per_assts = 0.2*assts
    per_mid_exam = 0.3*mid_exam
    per_final_exam = 0.45*final_exam
    per_clickers = 0.05*clickers
    tut_bonus = 0.1*tutorials
    final = per_assts+per_mid_exam+per_final_exam+per_clickers+tut_bonus
    final1 = min(final, 100)
    final_grade = round(final1)
    return final_grade

# Tests:
check.expect("Q3T1", basic_grade(0.0, 0.0, 0.0, 0.0, 0), 0)
check.expect("Q3T2", basic_grade(100.0, 100.0, 100.0, 100.0, 0), 100)
check.expect("Q3T3", basic_grade(100.0, 100.0, 100.0, 100.0, 12), 100)
check.expect("Q3T4", basic_grade(99.1, 98.9, 94.5, 99.2, 12), 98)