import check

error_msg = 'That is not correct.'
step1_msg = 'Think of a number. Multiply your number by 4:'
step2_msg = 'Add 9:'
step3_msg = 'Subtract the original number:'
step4_msg = 'Divide by 3:'
step5_msg = 'Subtract 3:'
final_msg = 'Your original number is {0}'

# number_game() calls pass_to_c2(c1) and will eventually lead to pass_to_c6(c5)
# Effect:
# * One value is read in
# numbe_game(): None -> None
def number_game(): 
    global c1
    c1 = input(step1_msg)
    pass_to_c2(c1)

# pass_to_c2(c1) reads in a value and may move on to next step or print/
# error_msg and start this step again
# Effect:
# * One value is read in 
# * One string may be printed
# pass_to_c2(c1): None -> None
# Example: The value input should be a natural number that is 9 units larger/
#          than the number in the last step
def pass_to_c2(c1):
    global c2
    c2 = input(step2_msg)
    if int(c2) == int(c1)+9:
        pass_to_c3(c2)
    else:
        print(error_msg)
        pass_to_c2(c1)
        
# pass_to_c3(c2) reads in a value and may move on to next step or print/
# error_msg and start this step again
# Effect:
# * One value is read in 
# * One string may be printed
# pass_to_c3(c2): None -> None
# Example: The value input should be a natural number that is less/
#          than the number in the last step by the number you firstly thinked of
def pass_to_c3(c2):
    global c3
    c3 = input(step3_msg)
    if int(c3) == int(c2)-(int(c2)-9)/4:
        pass_to_c4(c3)
    else:
        print(error_msg)
        pass_to_c3(c2)
        
# pass_to_c4(c3) reads in a value and may move on to next step or print/
# error_msg and start this step again
# Effect:
# * One value is read in 
# * One string may be printed
# pass_to_c4(c3): None -> None
# Example: The value input should be a natural number that is divided by 3/
# with the number from last step
def pass_to_c4(c3):
    global c4
    c4 = input(step4_msg)
    if int(c4) == int(c3)/3:
        pass_to_c5(c4)
    else:
        print(error_msg)
        pass_to_c4(c3)
        
# pass_to_c5(c4) reads in a value and may move on to next step or print/
# error_msg and start this step again
# Effect:
# * One value is read in 
# * One of 2 strings may be printed
# pass_to_c5(c4): None -> None
# Example: The value input should be a natural number that is 3 units less than/
# the number from last step
def pass_to_c5(c4):
    global c5
    c5 = input(step5_msg)
    if int(c5) == int(c4)-3:
        print(final_msg.format(c5))
    else:
        print(error_msg)
        pass_to_c5(c4)

# Tests:
check.set_screen('From step1_msg to step5_msg, and "Your orginal number is / 10" are printed')
check.set_input(["40", "49", "39", "13", "10"])
check.expect ("Q3T1", number_game(), None)

check.set_screen('From step1_msg to step5_msg with and error between step1/ and 2, and "Your orginal number is 10" are printed')
check.set_input(["40", "43" "49", "39", "13", "10"])
check.expect ("Q3T2", number_game(), None)

check.set_screen('From step1_msg to step5_msg with and error between step2/ and 3, and "Your orginal number is 10" are printed')
check.set_input(["40", "49", "34" "39", "13", "10"])
check.expect ("Q3T3", number_game(), None)

check.set_screen('From step1_msg to step5_msg with and error between step3/ and 4, and "Your orginal number is 10" are printed')
check.set_input(["40", "49", "39" "16", "13", "10"])
check.expect ("Q3T4", number_game(), None)

check.set_screen('From step1_msg to step5_msg with and error between step4/ and 5, and "Your orginal number is 10" are printed')
check.set_input(["40", "49", "39" "13", "19", "10"])
check.expect ("Q3T5", number_game(), None)