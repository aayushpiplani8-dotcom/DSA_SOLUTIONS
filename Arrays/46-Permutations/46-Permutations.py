# Last updated: 9/11/2026, 10:04:17 PM
1class Solution:
2    def permute(self, nums):
3        res = []
4        
5        def perms(i):
6            if i == len(nums):
7                res.append(nums[:])
8                return
9            for j in range(i, len(nums)):
10                nums[i], nums[j] = nums[j], nums[i]
11                perms(i + 1)
12                nums[i], nums[j] = nums[j], nums[i]
13        
14        perms(0)
15        return res