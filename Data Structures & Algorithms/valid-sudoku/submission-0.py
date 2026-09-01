class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # valid row:

        for i in range(9):
            seen = set()
            for j in range(9):
                spot = board[i][j]
                if spot in seen:
                    return False
                elif spot != ".":
                    seen.add(spot)

        # valid column:

        for i in range(9):
            seen = set()
            for j in range(9):
                spot = board[j][i]
                if spot in seen:
                    return False
                elif spot != ".":
                    seen.add(spot)
        
        starting = [(0,0),(0,3),(0,6),
        (3,0), (3,3),(3,6),
        (6,0),(6,3),(6,6)
        ]
        
        for i, j in starting:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    spot = board[row][col]
                    if spot in s:
                        return False
                    elif spot != ".":
                        s.add(spot)
                    
        return True



        
