# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        offsets = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def is_valid_coordinate(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
            
        
        def dfs(r, c, k):
            if len(word) - k == 0:
                return True

            if not is_valid_coordinate(r, c)\
            or board[r][c] == "*"\
            or board[r][c] != word[k]:
                return False

            board[r][c] = "*"

            for r_o, c_o in offsets:
                r_new, c_new = r + r_o, c + c_o
                if dfs(r_new, c_new, k+1):
                    return True
            
            board[r][c] = word[k]
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                
        return False
