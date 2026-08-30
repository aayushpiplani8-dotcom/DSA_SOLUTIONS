# Last updated: 8/30/2026, 9:25:42 AM
1from typing import List
2
3class Solution:
4    def twoSum(self, nums: List[int], target: int) -> List[int]:
5        # Fixed 1: enumerate(nums) instead of enumerate arr
6        nums_with_index = [(num, idx) for idx, num in enumerate(nums)]
7        nums_with_index.sort(key=lambda x: x[0])
8        
9        # Fixed 2: len(nums) instead of len(arr)
10        left, right = 0, len(nums) - 1
11        
12        while left < right:
13            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
14            if current_sum == target:
15                # Fixed 3: Added missing closing bracket ]
16                return [nums_with_index[left][1], nums_with_index[right][1]]
17            elif current_sum < target:
18                left += 1
19            else:
20                right -= 1
21                
22        return [-1, -1]