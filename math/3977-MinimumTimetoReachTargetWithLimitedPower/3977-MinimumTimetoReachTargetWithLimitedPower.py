# Last updated: 7/29/2026, 2:35:45 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4        res = ""
5
6        for i in range(n):
7            # Odd length palindrome
8            st = end = i
9            while st >= 0 and end < n and s[st] == s[end]:
10                st -= 1
11                end += 1
12            temp = s[st+1:end]
13            if len(temp) > len(res):
14                res = temp
15
16            # Even length palindrome
17            st, end = i, i+1
18            while st >= 0 and end < n and s[st] == s[end]:
19                st -= 1
20                end += 1
21            temp = s[st+1:end]
22            if len(temp) > len(res):
23                res = temp
24
25        return res
26        
27        