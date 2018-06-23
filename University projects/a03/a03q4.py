import check

# make_poem(s,n) prints the a string in a specific form
# Effect:
# * One string is printed:
# make_poem: Str Nat -> None
def make_poem(s,n):
    print(separate(0, 0, s, n))

# separate(a, b, s1, n1) returns a string that written in different lines
# after n1 words are tracked
# separate: Nat Nat Str Nat -> Str
def separate(a, b, s1, n1):
    if a == len(s1) - 1:
        return s1[len(s1) - 1]
    else:
        if s1[a] == " " and b == n1-1:
            return separate(a+1, b+1, s1, n1)
        elif s1[a] == " ":
            return s1[a]+separate(a+1, b+1, s1, n1)
        elif b == n1:
            return "\n"+s1[a]+separate(a+1, 0, s1, n1)
        else:
            return s1[a]+separate(a+1, b, s1, n1)

# Tests:
check.set_screen('"How many Lowes would Rob Lowe rob if Rob Lowe could rob/ Lowes" is printed with 1 word in each line')
check.expect("Q4T1", make_poem("How many Lowes would Rob Lowe rob if Rob Lowe/ could rob Lowes", 1), None) 

check.set_screen('"How many Lowes would Rob Lowe rob if Rob Lowe could rob/ Lowes" is printed with 3 word in each line')
check.expect("Q4T2", make_poem("How many Lowes would Rob Lowe rob if Rob Lowe/ could rob Lowes", 3), None) 

check.set_screen('"How many Lowes would Rob Lowe rob if Rob Lowe could rob/ Lowes" is printed with all words in 1 line')
check.expect("Q4T3", make_poem("How many Lowes would Rob Lowe rob if Rob Lowe/ could rob Lowes", 18), None) 