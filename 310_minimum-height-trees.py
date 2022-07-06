# https://leetcode.com/problems/minimum-height-trees/

from collections import deque
class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        
        adj_list = [set() for _ in range(0,n)]
        
        for start, end in edges:
            adj_list[start].add(end)
            adj_list[end].add(start)
            
        leaves = deque(leaf for leaf, neighbors in enumerate(adj_list) if len(neighbors) == 1)
        
        remaining = n
        
        while remaining > 2:
            next_leaves = deque()
            
            while len(leaves) > 0:
                leaf = leaves.popleft()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                
                if len(adj_list[neighbor]) == 1:
                    next_leaves.append(neighbor)

                remaining -= 1
            
            leaves = next_leaves
        
        return list(leaves)
    
    
    def findMinHeightTreesInefficient(self, n: int, edges: List[List[int]]) -> List[int]:
        res = None
        res_min = 2 * (10 ** 4) + 1
        
        # adjecency list for e1-e2, undirected
        adj_list = [[] for x in range(0,n)]
        
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        visited = None
        def dfs(node):
            visited.add(node)
            # contains subproblem solutions
            local_res = [0] + [dfs(next_node) + 1 for next_node in adj_list[node] if next_node not in visited]
            return max(local_res)
        
        for x in range(n):
            visited = set()
            ret = dfs(x)
            if ret < res_min:
                res = []
                res_min = ret
            
            if ret == res_min:
                res.append(x)
        
        return res
