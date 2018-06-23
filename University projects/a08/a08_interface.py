#q1a
def shift_encode(s):
    pass


#q1b

def shift_decode(s):
    pass






#q2

# ## a Bingocard is a (dictof Str (listof (anyof Nat 'XX'))) and 		
# ## represents a standard bingo card in 75 ball bingo
# ## requires: 
# ##	- it has exactly 5 key value pairs
# ##	- the keys are the capital letters 'B' 'I' 'N' 'G' 'O'
# ## 	- each list is length 5 and is made up of the string 'XX' or 
# ##	  numbers 1 through 75 according to the breakdown below
# ##	- key 'B' only has numbers between 1 and 15 inclusive 
# ##	- key 'I' only has numbers between 16 and 30 inclusive
# ##	- key 'N' only has numbers between 31 and 45 inclusive
# ##	- key 'G' only has numbers between 46 and 60 inclusive
# ##	- key 'O' only has numbers between 61 and 75 inclusive
# ##	- the associated list at key 'N' will always have its element at 
# ##	  index 2 equal to 'XX' (representing the free space)
# ##	- the numbers in each list must be unique



# display_bingo_card(crd) prints a nicely formatted version of crd
# Effects: 6 lines are printed
# display_bingo_card: Bingocard -> None

def display_bingo_card(crd):
    
    header = "  B  I  N  G  O  "
    
    print(header)
    
    for i in range(5):
        line = " {0:2} {1:2} {2:2} {3:2} {4:2}  ".format(crd['B'][i],
                                                         crd['I'][i],
                                                         crd['N'][i],
                                                         crd['G'][i],
                                                         crd['O'][i])
        print(line)
        
        
        
    
    
    
    


row_win = "Winner: Row {0}."
column_win = "Winner: Column {0}."
no_win = "Not a winner."


def play_bingo(crd,lon):
    pass
        
        
       
    
    
            


            
            
            

from random import randint

# make_bingo_card() returns a randomized Bingocard
# make_bingo_card: None -> Bingocard
def make_bingo_card():
    interval_width = 15
    card = {}
    for i in range(5):
        L = []
        while len(L) < 5:
            n = randint(interval_width*i+1,interval_width*(i+1))
            if not n in L:
                L.append(n)
                
        if i == 0:
            card['B'] = L
        elif i == 1:
            card['I'] = L
        elif i == 2:
            L[2] = 'XX'
            card['N'] = L
        elif i == 3:
            card['G'] = L
        else:
            card['O'] = L
    
    return card



    
    






#q3

class Vector:
    '''Fields: x(Int), y(Int)'''
    def __init__(self,xVal,yVal):
        self.x = xVal
        self.y = yVal
        
    def __eq__(self,other):
        if isinstance(other,Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __repr__(self):
        return "Vector({0},{1})".format(self.x,self.y)
          
    
    
    #q3b
    
    # NOTE: for these functions you still need the full design recipe
    # however the Tests section will have to be done OUTSIDE of the class
    
    def __add__(self,other):
        pass
    
    def __mul__(self,other):
        pass
    
    def length(self):
        pass
    
    def scale(self,k):
        pass
    
    
#q3a
def add_vectors(v1,v2):
    pass

def dot_product(v1,v2):
    pass

def length(vec):
    pass

def scale(vec,k):
    pass




#q4

acute_cat = 'ACUTE'
obtuse_cat = 'OBTUSE'
right_cat = 'RIGHT'
par_cat = 'PARALLEL'


def classify_angles(lov,vec):
    pass
            

        



    
    
        