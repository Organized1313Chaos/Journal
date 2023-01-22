# ====================================================
'''
Leetcode Contest
Date: January 22, 2023
Problem Number: 2541
Name:  Minimum Operations to Make Array Equal II 
Link: https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/description/
'''
# ====================================================

# ====================================================
'''
Approach 1: Successful Approach, Number theory Approach
num2 = num1  + (mul)*k
Condition: pos mul == neg mul, return pos
No of Test Cases Passed: All
'''

'''
NOTES:

MISTAKES:
if 0: Never check the half condition like this
Always write down the full condition

Never forget Arithmatic Exception namely--> DivisionByZeroException
'''

# ====================================================

# Mistake: if 0 returns False
class Solution:
    def minOperations(self, nums1, nums2, k: int) -> int:
        if nums1==nums2: return 0
        if k==0 and nums1!=nums2: return -1
        pos = 0
        t_sum = 0
        
        for num1, num2 in zip(nums1, nums2):
            rem = num1 - num2
            if k!=0:
                if (rem%k)!=0:
                    return -1
                diff = rem//k
            else:
                diff = rem
            
            if diff>0:
                pos+=diff
            t_sum += diff
            
        if t_sum!=0: 
            return -1
        
        return pos