# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        l_ivl = len(intervals)
        r_ivl = 0
        ivl_idx = 0
        s_new, e_new = newInterval 
        
        while ivl_idx < len(intervals):
            s, e = intervals[ivl_idx]
            
            if l_ivl == len(intervals):
                if s_new <= e:
                    l_ivl = ivl_idx

            if e_new >= s:
                r_ivl = ivl_idx + 1

            ivl_idx += 1
            
        if l_ivl >= len(intervals):
            return intervals + [newInterval]
        
        if r_ivl <= 0:
            return [newInterval] + intervals
        
        if l_ivl == r_ivl:
            return intervals[:l_ivl] + [newInterval] + intervals[l_ivl:]
        
        return intervals[:l_ivl] + [[min(intervals[l_ivl][0], s_new), max(intervals[r_ivl-1][1], e_new)]] + intervals[r_ivl:]
        
