# Last updated: 8/21/2026, 11:49:26 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        memo = {}
4        return self.helper(n, memo)
5    
6    def helper(self, n: int, memo: dict[int, int]) -> int:
7        if n == 0 or n == 1:
8            return 1
9        if n not in memo:
10            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
11        return memo[n]