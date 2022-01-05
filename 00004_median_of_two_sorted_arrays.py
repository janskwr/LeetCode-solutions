"""
SOLUTION 1 - BINARY SEARCH
Time Complexity: O(logn)
Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        imin = 0
        imax = m
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                    
                if (n + m) % 2 == 1:
                    return max_of_left
                
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:    
                    min_of_right = min(nums2[j], nums1[i])
                    
                return (max_of_left + min_of_right) / 2.0
