"""
SOLUTION 1
Time Complexity: O(n)
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
            
