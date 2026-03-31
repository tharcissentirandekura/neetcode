class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validrow(board):
            for row in board:
                seen = set()
                for num in row:
                    # print(num, end =" ")
                    if num != '.':
                        if not (int(num) < 10 and int(num) > 0):
                            return False
                        if num in seen:
                            return False
                        seen.add(num)
                # print("\n")
            return True
                
        # check colums
        def validcolumns(board):
            
            for row in range(len(board)):
                seen = set()
                for col in range(len(board)):
                    num = board[col][row]
                    # print(num, end =" "
                    if num != '.':
                        if num in seen:
                            return False
                        if not (int(num) < 10 and int(num) > 0):
                            return False
                        # if num in seen:
                        #     return False
                        seen.add(num)
            return True

        # check 3 x 3 sub boxs
        def validbox(board,row_start,row_end,col):
            if row_end > 9:
                return True
            seen = set()
            for i in range(row_start,row_end):
                for j in range(col,col + 3):
                    num = board[i][j]
                    print(num, end=" ")
                    if num != '.':
                        if num in seen:
                            return False 
                        if not (int(num) < 10 and int(num) > 0):
                            return False          
                        seen.add(num)
                print("\n")

            return validbox(board, row_start + 3,row_end + 3, col)
        
        return (validcolumns(board) and 
                validrow(board) and
                validbox(board,0,3,0) and 
                validbox(board,0,3,3) and
                validbox(board,0,3,6))