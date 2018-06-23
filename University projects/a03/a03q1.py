import check

invalid_msg = "Invalid password"
end_msg = "Thank you!"
welcome_msg = "Enter a password:"

# check_lower(s, i) returns the number of times that lower_case_letters/
# appears in the string
# check_lower: Str Nat -> anyof (Nat -1)
def check_lower(s, i):
    if i == -1:
        return 0
    else:
        if s[i].islower():
            return 1 + check_lower(s, i-1)
        else:
            return check_lower(s, i-1)

# check_upper(s, i) returns the number of times that upper_case_letters/
# appears in the string
# check_upper: Str Nat -> anyof (Nat -1)
def check_upper(s, i):
    if i == -1:
        return 0
    else:
        if s[i].isupper():
            return 1 + check_upper(s, i-1)
        else:
            return check_upper(s, i-1)

# check_num(s, i) returns the number of times that numbers/
# appears in the string
# check_num: Str Nat -> anyof (Nat -1)
def check_num(s, i):
    if i == -1:
        return 0
    else:
        if s[i].isdigit():
            return 1 + check_num(s, i-1)
        else:
            return check_num(s, i-1)

# check_space(s, i) returns the number of times that lower_case_letters/
# appears in the string
# check_space: Str Nat -> Bool
def check_space(s, i):
    if i == -1:
        return True
    else:
        if s[i] == " ":
            return False
        else:
            return check_space(s, i-1)

# pass_check() reads in a string and gives if it passes the requirements
# Effect:
# * One value is read in 
# * Two Stings are printed
# pass_check(): None -> Str
# Example: the function will give "Thank you!" only when all the checks above/
#          are met
def pass_check():
    s = input(welcome_msg)
    i = len(s) - 1
    if check_lower(s, i) > 0 and check_upper(s, i) > 0 and check_num(s, i) > 0 and check_space(s, i):
        print(end_msg)
    else:
        print(invalid_msg)
        return pass_check()
    return s

# Tests:
check.set_screen('welcome_msg and end_msg are printed')
check.set_input(['Boc123'])
check.expect("Q1T1", pass_check(), 'Boc123')

check.set_screen('welcome_msg and end_msg are printed with 1 error because of/ missing upper case')
check.set_input(['boc123', 'Boc123'])
check.expect("Q1T2", pass_check(), 'Boc123')

check.set_screen('welcome_msg and end_msg are printed with 1 error because of/ missing lower case')
check.set_input(['BOC123', 'Boc123'])
check.expect("Q1T3", pass_check(), 'Boc123')

check.set_screen('welcome_msg and end_msg are printed with 1 error because of/ missing number')
check.set_input(['Bocgoof', 'Boc123'])
check.expect("Q1T4", pass_check(), 'Boc123')

check.set_screen('welcome_msg and end_msg are printed with 1 error because of/ space observed')
check.set_input(['Bo c123', 'Boc123'])
check.expect("Q1T5", pass_check(), 'Boc123')