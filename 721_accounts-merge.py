# https://leetcode.com/problems/accounts-merge/
class Node:
    def __init__(self, email=None, name=None):
        self.email = email
        self.name = name
        self.neighbors = []


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_graph = {}
        parent_nodes = []
        for account in accounts:
            name, *emails = account
            parent_email = emails[0]
            
            if parent_email not in email_graph:
                email_graph[parent_email] = Node(email=parent_email, name=name)

            parent_node = email_graph[parent_email]
            
            for email in emails[1:]:
                if email not in email_graph:
                    email_graph[email] = Node(email=email, name=name)
                
                email_node = email_graph[email]
                parent_node.neighbors.append(email_node)
                email_node.neighbors.append(parent_node)
        
        res = []
        visited = set()
        
        
        def dfs(root, res_part):
            visited.add(root)
            res_part.append(root.email)
            for neighbor in root.neighbors:
                if neighbor not in visited:
                    dfs(neighbor, res_part)
            return res_part

        
        for email, email_node in email_graph.items():
            if email_node not in visited:
                res_part_1 = [email_node.name]
                res_part_2 = dfs(email_node, [])
                res_part_2.sort()
                res.append(res_part_1 + res_part_2)
        
        return res
        