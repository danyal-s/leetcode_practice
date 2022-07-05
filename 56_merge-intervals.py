# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        res = []

        def merge_intervals(ivl1, ivl2):
            return ivl1[0], max(ivl1[1], ivl2[1])
        
        for ivl in intervals[1:]:
            xs1, xe1 = prev
            xs2, xe2 = ivl
            if xs2 <= xe1 and xs2 >= xs1:
                prev = merge_intervals(prev, ivl)
            else:
                res.append(prev)
                prev = xs2, xe2
        
        res.append(prev)
        return res
                
            