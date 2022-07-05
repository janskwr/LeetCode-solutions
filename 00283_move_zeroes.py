"""
SOLUTION 1 - DELETING ZEROS AND APPENDING
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # count zeros
        counter = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                n -= 1
                counter += 1
            else:
                i += 1
        
        for i in range(counter):
            nums.append(0)
            
            
            
            
"""
SOLUTION 2 - SLOW AND FAST POINTERS
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1

