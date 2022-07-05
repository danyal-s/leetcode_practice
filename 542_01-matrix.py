# https://leetcode.com/problems/01-matrix/

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1

        
        def get_neighbors(r, c):
            neighbors = []
            
            if r - 1 >= 0:
                val = (r-1, c)
                neighbors.append(val)
                
            if r + 1 < len(mat):
                val = (r+1, c)
                neighbors.append(val)
                
            if c - 1 >= 0:
                val = (r, c-1)
                neighbors.append(val)
            
            if c + 1 < len(mat[0]):
                val = (r, c+1)
                neighbors.append(val)
            
            return neighbors
            
        
        while len(q) != 0:
            r, c = q.popleft()
            neighbors = get_neighbors(r, c)
            for nr, nc in neighbors:
                if mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        
        return mat
