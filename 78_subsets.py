# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def search(i, sol):
            for x in range(i, len(nums)):
                sol.append(nums[x])
                yield sol.copy()
                yield from search(x+1, sol)
                sol.pop()

        return [[]] + list(search(0, []))
