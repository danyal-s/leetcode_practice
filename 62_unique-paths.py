# https://leetcode.com/problems/unique-paths/
from collections import deque
class Solution:
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        # dp
        search = [[0 for y in range(m+1)] for x in range(n+1)]
        search[n-1][m-1] = 1
        
        for x in reversed(range(n)):
            for y in reversed(range(m)):
                search[x][y] += search[x+1][y]
                search[x][y] += search[x][y+1]
                
        return search[0][0]
    
    
    
    def uniquePathsBFS(self, m: int, n: int) -> int:
        
        search = [[0 for y in range(m + 1)] for x in range(n + 1)]

        search[n-1][m-1] = 1
        
        q = deque()
        q.append((n-1, m-1))
        visited = set()
        
        while len(q) > 0:
            x, y = q.popleft()
            search[x][y] += search[x+1][y] + search[x][y+1]
            
            if x-1 >= 0 and (x-1, y) not in visited:
                q.append((x-1, y))
                visited.add((x-1, y))
            
            if y-1 >= 0 and (x, y-1) not in visited:
                q.append((x, y-1))
                visited.add((x-1, y))
            
        
        return search[0][0]
