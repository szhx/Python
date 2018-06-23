import check

grid3x3 = [[True ,False,False],[False,False,False],[False,False,True]] 

# reveal(grid,board, row, col) reveals the tile at the given row and col(umn)
#   in board, using the mine positions from grid
# reveal: MineGrid MineBoard -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# effects: board is mutated

def reveal(grid,board,row,col):
    if grid[row][col]:
        board[row][col] = '*'
    else:
        board[row][col] = str(count_mines(grid,row,col))

# is_mine(lst,a,b) returns 1 if the (a,b) index in the list is true and returns/
# 0 otherwise
# is_mine: listof (Bool) Nat Nat -> Nat
# Example: is_mine(grid3x3,0,0) => 1
def is_mine(lst,a,b):
    if lst[a][b] == True:
        return 1
    else:
        return 0

# count_mines(grid,row,col) returns the number of mines around a specific/
# position
# count_mines: listof (listof (Bool)) Nat Nat -> Nat
# Require: all lists are non-empty
# Example: count_mines(grid3x3,1,1) => 2 
def count_mines(grid,row,col):
    if row-1 >= 0 and col-1 >= 0:
        a00 = is_mine(grid,row-1,col-1)
    else:
        a00 = 0
    if row-1 >= 0:
        a01 = is_mine(grid,row-1,col)
    else:
        a01 = 0
    if row-1 >= 0 and col+1 < len(grid[0]):
        a02 = is_mine(grid,row-1,col+1)
    else:
        a02 = 0    
    if col-1 >= 0:
        a10 = is_mine(grid,row,col-1)
    else:
        a10 = 0
    if col+1 < len(grid[0]):
        a12 = is_mine(grid,row,col+1)
    else:
        a12 = 0
    if row+1 < len(grid) and col-1 >= 0:
        a20 = is_mine(grid,row+1,col-1)
    else:
        a20 = 0
    if row+1 < len(grid):
        a21 = is_mine(grid,row+1,col)
    else:
        a21 = 0
    if row+1 < len(grid) and col+1 < len(grid[0]):
        a22 = is_mine(grid,row+1,col+1)
    else:
        a22 = 0
    return a00+a01+a02+a10+a12+a20+a21+a22

# Tests:
check.expect("Q3T1", count_mines(grid3x3,0,0), 0)
check.expect("Q3T2", count_mines(grid3x3,0,2), 0)
check.expect("Q3T3", count_mines(grid3x3,1,2), 1)
