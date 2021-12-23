"""
SOLUTION 1
Time Complexity: O(n)
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        if stack:
            for i in range(len(stack)):
                s[stack[i]] = ''
        return ''.join(s)
    
