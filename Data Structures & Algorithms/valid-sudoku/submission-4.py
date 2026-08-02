class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #board[x][y] where x is the row # indexed at 0
        # y is the column # indexed at 0

        # row checker (O(n^2)) 
        for row in board:
            seen = set()
            for space in row:
                if(space == "."):
                    continue
                else:
                    if(space not in seen):
                        seen.add(space)
                    else:
                        return False
        
        # column checker (O(n^2))
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                else:
                    if(board[j][i] not in seen):
                        seen.add(board[j][i])
                    else:
                        return False

        #(1,1),(1,4),(1,7)
        #(4,1),(4,4),(4,7)
        #(7,1),(7,4),(7,7)
        for x in range(1,8, 3):
            for y in range(1,8,3):
                seen = set()
                for i in range(-1,2):
                    if(x+i < 0):
                        continue
                    for j in range(-1,2):
                        if(y+j < 0):
                            continue
                        if board[x+i][y+j] == ".":
                            continue
                        elif(board[x+i][y+j] not in seen):
                            seen.add(board[x+i][y+j])
                        else:
                            return False


        return True

        
        # column checker

