"""
SOLUTION 1 - HASH TABLE
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            result = target - nums[i]
            if result in hashmap:
                return [i, hashmap[result]]
            hashmap[nums[i]] = i
            

"""
SOLUTION 2 - BRUTE FORCE
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
 
