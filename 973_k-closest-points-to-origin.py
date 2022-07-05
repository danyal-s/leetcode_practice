# https://leetcode.com/problems/k-closest-points-to-origin/
import math
import heapq

class Solution:
    def kClosestMergeSort(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        
        for x, y in points:
            dist = math.sqrt(x**2 + y ** 2)
            res.append((dist, (x, y)))
        
        res.sort(key=lambda x: x[0])
        
        return [x[1] for x in res][0:k]
            


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x, y in points:
            dist = heapq.heappush(res, (math.sqrt(x**2 + y ** 2), (x,y)))


        return [heapq.heappop(res)[1] for _ in range(k)]
