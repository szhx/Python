import check
import math

# how_many_phones(phone_length, distance) returns the exact number of 
# phones with known length needed to cover a certain distance
# how_many_phones: Float Float -> Nat
# requires: phone_length is measured in centimeter and is not zero
#           distance is measured in kilometer
# Examples: how_many_phones(14.7, 1.6) => 10885

def how_many_phones(phone_length, distance):
    num = (1000*distance)/(phone_length/100) 
    number_of_phone = math.ceil(num)
    return number_of_phone

# Tests: 
check.expect("Q1T1",how_many_phones(1,0),0)
check.expect("Q1T2",how_many_phones(100,23),23000)
check.expect("Q1T3",how_many_phones(100,2.3),2300)
check.expect("Q1T4",how_many_phones(13.4,2.7),20150)