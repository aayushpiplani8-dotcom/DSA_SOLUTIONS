# Last updated: 9/2/2026, 9:47:06 PM
1from typing import List
2
3
4class Solution:
5
6  def nextPermutation(self, nums: List[int]) -> None:
7    n = len(nums)
8    pivot = -1
9
10    # Step 1: Find the first decreasing element from the right
11    for i in range(n - 2, -1, -1):
12      if nums[i] < nums[i + 1]:
13        pivot = i
14        break
15
16    # Step 2: If no pivot is found, the array is in reverse order
17    if pivot == -1:
18      nums.reverse()
19      return
20
21    # Step 3: Find the smallest element larger than nums[pivot] from the right
22    for j in range(n - 1, pivot, -1):
23      if nums[j] > nums[pivot]:
24        nums[j], nums[pivot] = nums[pivot], nums[j]
25        break
26
27    # Step 4: Reverse the sub-array to the right of the pivot
28    nums[pivot + 1 :] = reversed(nums[pivot + 1 :])