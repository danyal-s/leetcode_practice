# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = [[] for x in range(numCourses)]
        rec_stack = set()
        visited = set()
        for course, dep_course in prerequisites:
            adj_list[dep_course].append(course)
        
        def dfs(n):
            nonlocal rec_stack
            nonlocal visited
            rec_stack.add(n)
            visited.add(n)

            for c in adj_list[n]:
                if c in rec_stack:
                    return False

                if c not in visited:
                    res = dfs(c)
                    if not res:
                        return False
            
            rec_stack.remove(n)
            
            return True

        for dep_course in range(len(adj_list)):
            if dep_course not in visited:
                res = dfs(dep_course)
            else:
                continue
    
            if not res:
                return False
            else:
                continue
        
        return True
