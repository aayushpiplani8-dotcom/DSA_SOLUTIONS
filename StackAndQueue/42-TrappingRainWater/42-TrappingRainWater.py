# Last updated: 9/21/2026, 6:04:40 PM
1class Solution:
2    def trap(self, height: list[int]) -> int:
3
4        n = len(height)
5
6        if n == 0:
7            return 0
8
9        # TWO POINTERS
10        left = 0
11        right = n - 1
12
13        # Maximum height seen from both sides
14        left_Max = 0
15        right_Max = 0
16
17        water = 0
18
19        while left <= right:
20
21            # Process the smaller side
22            if height[left] <= height[right]:
23
24                # New maximum found on left
25                if height[left] >= left_Max:
26                    left_Max = height[left]
27
28                # Water can be trapped
29                else:
30                    water += left_Max - height[left]
31
32                left += 1
33
34            else:
35
36                # New maximum found on right
37                if height[right] >= right_Max:
38                    right_Max = height[right]
39
40                # Water can be trapped
41                else:
42                    water += right_Max - height[right]
43
44                right -= 1
45
46        return water
47        