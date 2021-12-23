"""
SOLUTION 1
Time Complexity: O(n)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left: right]
                two = s[left + 1: right + 1]
                if one == one[::-1] or two == two[::-1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True
            
