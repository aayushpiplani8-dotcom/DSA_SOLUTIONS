# Last updated: 7/29/2026, 3:13:05 AM
1class Solution:
2    def fib(self, n: int) -> int:
3        if n < 2:
4            return n
5        
6        prev2 = 0  # Represents fib(0)
7        prev1 = 1  # Represents fib(1)
8        
9        for i in range(2, n + 1):
10            curr = prev1 + prev2
11            prev2 = prev1
12            prev1 = curr
13            
14        return prev1
15
16
17
18
19
20        