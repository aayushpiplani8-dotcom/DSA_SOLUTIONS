# Last updated: 7/31/2026, 1:08:12 AM
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        prev2 = 0  # Represents fib(0)
        prev1 = 1  # Represents fib(1)
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return prev1





        