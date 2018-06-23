import check

# earned_grade(assts, mid_exam, final_exam, clickers, tutorials) returns the 
# final grade of the student in this term in CS116, and the weighted average 
# score of midterm and final need to pass
# earn_grade: Float Float Float Float Nat -> Int
# requires: 0 <= assts <= 100
#           0 <= mid_exam <= 100
#           0 <= final_exam <= 100
#           0 <= clickers <= 100
#           0 <= tutorials <= 12
# Examples: basic_grade(60.0, 75.8, 90.0, 55.5, 9) => 79

def earned_grade(assts, mid_exam, final_exam, clickers, tutorials):
    grade_before_round = 0.2 * assts + 0.3 * mid_exam + 0.45 * final_exam + 0.05 * clickers + 0.1 * tutorials
    grade_rounded = round(grade_before_round)
    grade = min(grade_rounded, 100)
    weighted_average = (0.3 * mid_exam + 0.45 * final_exam) / 0.7
    if weighted_average < 50 and grade >= 45:
        final_grade = 45
    else:
        final_grade = grade
    return final_grade

# Tests:
check.expect("Q1T1", earned_grade(60.0, 55.8, 40.0, 55.5, 9), 45)
check.expect("Q1T2", earned_grade(10.0, 5.0, 40.0, 12.0, 0), 22)
check.expect("Q1T3", earned_grade(50.0, 50.0, 50.0, 50.0, 0), 50)
check.expect("Q1T4", earned_grade(45.0, 45.0, 45.0, 45.0, 0), 45)
check.expect("Q1T5", earned_grade(95.3, 78.9, 65.7, 83.2, 6), 77)
check.expect("Q3T2", earned_grade(100.0, 100.0, 100.0, 100.0, 0), 100)
check.expect("Q3T3", earned_grade(100.0, 100.0, 100.0, 100.0, 12), 100)