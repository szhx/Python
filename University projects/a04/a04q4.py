import check

grid3x3 = [[True ,False,False],[False,False,False],[False,False,True]] 
board3x3 = [[' ','1','0'],[' ','2','1'],[' ',' ','*']] 
board3x31 = [[' ','1','0'],['0','2','1'],['1','1',' ']]
board3x32 = [[' ','1',' '],['0','2','1'],['1','1',' ']]

# game_lost(board) returns true if board contains one or more revealed mines,
#   false otherwise
# game_lost: GameBoard -> Bool

def game_lost(board):
    mined_rows = len(list(filter(lambda row: '*' in row, board)))
    return mined_rows != 0

# track_mine_row(a) returns the number of mines in a row
# track_mine_row: listof (Bool) -> Nat
# Require: list is non-empty
# Example: track_mine_row(['True','True']) => 2
def track_mine_row(a):
    if a == []:
        return 0
    elif a[0] == True:
        return 1+track_mine_row(a[1:])
    else:
        return track_mine_row(a[1:])
    
# track_mine(grid) returns the number of mines in a grid
# track_mine: listof (lisof (Bool)) -> Nat
# Require: list is non-empty
# Example: track_mine(['True','True'],['True','True']) => 4
def track_mine(grid):
    if grid == []:
        return 0
    else:
        return track_mine_row(grid[0])+track_mine(grid[1:])

# track_space_row(b) returns the number of spaces in a row
# track_mine_row: listof (Nat) -> Nat
# Require: list is non-empty
# Example: track_mine_row([' ','1']) => 1
def track_space_row(b):
    if b == []:
        return 0
    elif b[0] == ' ':
        return 1+track_space_row(b[1:])
    else:
        return track_space_row(b[1:])
    
# track_space(board) returns the number of spaces in a row
# track_mine: listof (listof (Nat)) -> Nat
# Require: list is non-empty
# Example: track_mine_row([' ','1'],['5','1'] => 1
def track_space(board):
    if board == []:
        return 0
    else:
        return track_space_row(board[0])+track_space(board[1:])

# game_won(grid,board) returns true only when all the non-mine positions are/
# revealed and the mine postions are spaces
# game_won: listof (listof (Bool)) listof (listof (Nat)) -> Bool
# Require: all lists are non-empty
# Example: game_won(grid3x3,board3x3) => False
def game_won(grid,board):
    if game_lost(board) > 0:
        return False
    elif track_mine(grid) == track_space(board):
        return True
    else:
        return False
    
# Tests:
check.expect("Q4T1", game_won(grid3x3,board3x3), False)
check.expect("Q4T2", game_won(grid3x3,board3x31), True)
check.expect("Q4T3", game_won(grid3x3,board3x32), False)