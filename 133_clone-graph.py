# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import Queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        q = Queue()
        q.put(node)
        
        node_dict = {node.val:Node(node.val)}
        
        
        while q.qsize() > 0:
            n = q.get()
            n_copy = node_dict[n.val]
            for neighbor_n in n.neighbors:
                if neighbor_n.val not in node_dict:
                    node_dict[neighbor_n.val] = Node(neighbor_n.val)
                    q.put(neighbor_n)
            
                n_copy.neighbors.append(node_dict[neighbor_n.val])
            
        return node_dict[node.val]
