# ====================================================
'''
Leetcode Contest: Biweekly 96
Date: January 22, 2023
Problem Number: 2540 
Name: Minimum Common Value
Link: https://leetcode.com/problems/minimum-common-value/description/
'''
# ====================================================


# ====================================================
'''
Approach 1: Successful Approach, Using Pointers
No of Test Cases Passed: All
'''

'''
NOTES:

MISTAKES:

'''

# ====================================================

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        l1, l2 = 0, 0
        
        while l1<N and l2<M:
            if nums1[l1]==nums2[l2]:
                return nums1[l1]
            if nums1[l1]>nums2[l2]:
                l2+=1
                continue
            l1+=1
            
        return -1