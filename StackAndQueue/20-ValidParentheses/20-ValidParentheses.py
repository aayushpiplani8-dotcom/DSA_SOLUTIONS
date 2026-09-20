# Last updated: 9/21/2026, 1:36:54 AM
1class Solution:
2
3    def isValid(self, s: str) -> bool:
4
5        stack = []
6
7        for ch in s:
8
9            # Opening brackets → PUSH
10            if ch == '(' or ch == '{' or ch == '[':
11                stack.append(ch)
12
13            # Closing brackets
14            else:
15
16                # Closing bracket but stack is empty
17                if not stack:
18                    return False
19
20                # Check matching pairs
21                if ch == ')' and stack[-1] != '(':
22                    return False
23
24                if ch == '}' and stack[-1] != '{':
25                    return False
26
27                if ch == ']' and stack[-1] != '[':
28                    return False
29
30                # Matching pair found
31                stack.pop()
32
33        # Stack should be empty at the end
34        return len(stack) == 0