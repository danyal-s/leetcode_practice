# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        offsets = ((0,1),(1,0),(-1,0),(0,-1))
        
        def is_valid_coordinate(r, c):
            nonlocal grid
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
        
        def dfs(r, c):
            nonlocal grid, offsets
            grid[r][c] = "0"
            
            for r_offset, c_offset in offsets:
                r_new, c_new = (r + r_offset, c + c_offset)
                if is_valid_coordinate(r_new, c_new) \
                and grid[r_new][c_new] == "1":
                    dfs(r_new, c_new)

        island_count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)
                
        
        return island_count
