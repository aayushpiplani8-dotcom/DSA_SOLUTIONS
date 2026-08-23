# Last updated: 8/23/2026, 9:05:45 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res = []
4
5        def dfs(openP, closeP, s):
6            if openP == closeP and openP + closeP == n * 2:
7                res.append(s)
8                return
9            
10            if openP < n:
11                dfs(openP + 1, closeP, s + "(")
12            
13            if closeP < openP:
14                dfs(openP, closeP + 1, s + ")")
15
16        dfs(0, 0, "")
17
18        return res