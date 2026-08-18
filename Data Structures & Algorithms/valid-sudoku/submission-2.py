class Solution:


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":continue
                if not good_vh(board,i,j) or not good_block(board,i,j):
                    return False
                
        return True

def good_vh(board,i,j):
    e = board[i][j]
    for y in range(9):
        if y != j and board[i][j] == board[i][y]: return False
    for x in range(9):
        if x != i and board[i][j] == board[x][j]: return False
    return True

def stpt(j):
    if j>=6: y=6
    elif j>=3: y=3
    else: y = 0
    return y

def good_block(board,i,j):
    x,y = stpt(i),stpt(j)
    for p in range(x,x+3):
        for q in range(y,y+3):
            if board[i][j] == board[p][q] and (p != i or q != j): return False
    return True