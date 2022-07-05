"""
SOLUTION 1 - LONGEST COMMON SUBSTRING IMPROVED
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
    	n = len(s)
    	max_len = 0
    	longest = ""
    	rev = s[::-1]
    	dp = [0 for i in range(n)]
    	for i in range(n):
    	    	



"""
SOLUTION 2 - LONGEST COMMON SUBSTRING
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        dp = [[0 for i in range(n)] for j in range(n)]
        longest = ""
        max_len = 0
        for i in range(n):
            for j in range(n):
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    if i - dp[i][j] + 1 == n - j - 1:
                        max_len = dp[i][j]
                        longest = s[i - max_len + 1:i + 1]
        return longest

    

"""
SOLUTION 3 - BRUTE FORCE
Time Complexity: O(n^3)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        for i in range(n):
            for j in range(i, n):
                temp = s[i:j + 1]
                if temp == temp[::-1]:
                    if len(temp) > len(longest):
                        longest = temp
        return longest

