# Last updated: 9/25/2026, 3:52:05 AM
1class Solution:
2    def longestConsecutive(self, nums):
3
4        # STEP 1: Store all elements in a hash set
5        # Set also removes duplicate elements
6        hash_set = set(nums)
7
8        longest = 0
9
10        # STEP 2: Traverse through each unique number
11        for num in hash_set:
12
13            # STEP 3: Check if num is the START of a sequence
14            # If num - 1 exists, then num is not the starting point
15            if num - 1 not in hash_set:
16
17                current = num
18                count = 1
19
20                # STEP 4: Keep searching for consecutive elements
21                # current + 1, current + 2, ...
22                while current + 1 in hash_set:
23                    current += 1
24                    count += 1
25
26                # STEP 5: Update the longest sequence length
27                longest = max(longest, count)
28
29        # STEP 6: Return longest length
30        return longest