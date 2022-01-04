"""
SOLUTION 1 - SLIDING WINDOW
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(i, mp[s[j]])
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
        
        
"""
SOLUTION 2 - BRUTE FORCE
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        begin = 0
        result = 0
        temp = None
        for i in range(n):
            for j in range(i):
                if s[j] == s[i]:
                    temp = j
            if temp is not None:
                begin = max(begin, temp + 1)
            result = max(result, i - begin + 1)
        return result
