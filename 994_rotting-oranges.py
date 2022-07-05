# https://leetcode.com/problems/rotting-oranges/
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges_count = len([val for r in grid for val in r if val == 1])
        
        if fresh_oranges_count == 0:
            return 0
        
        
        def is_valid_coordinates(r, c):
            nonlocal grid
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
            
        
        
        prev_fresh_oranges_count = -1
        q = deque()
        
        offsets = ((0,1),(1,0),(-1,0),(0,-1))
        minutes = 0
        q.extend((ri, ci) for ri, r in enumerate(grid) for ci, val in enumerate(r) if val == 2)
        
        while prev_fresh_oranges_count != fresh_oranges_count \
                and fresh_oranges_count > 0:
            
            prev_fresh_oranges_count = fresh_oranges_count
            
            local_q = q.copy()
            while len(local_q) > 0:
                ri_ro, ci_ro = local_q.popleft()
                
                for ri_os, ci_os in offsets:
                    ri_ro_os, ci_ro_os = ri_ro + ri_os, ci_ro + ci_os
                    if is_valid_coordinates(ri_ro_os, ci_ro_os) \
                        and grid[ri_ro_os][ci_ro_os] == 1:
                        grid[ri_ro_os][ci_ro_os] = 2
                        q.append((ri_ro_os, ci_ro_os))
                        fresh_oranges_count -= 1
                    
            minutes += 1

        
        return minutes if fresh_oranges_count == 0 else -1
