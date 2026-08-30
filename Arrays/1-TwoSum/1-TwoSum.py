# Last updated: 8/30/2026, 9:27:19 AM
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        seen = {}  # Map: number -> index
4        
5        for i, num in enumerate(nums):
6            diff = target - num
7            if diff in seen:
8                return [seen[diff], i]
9            seen[num] = i
10            
11        return [-1, -1]