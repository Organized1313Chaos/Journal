# ====================================================
'''
Leetcode Question
Date: January 11, 2023
Problem Number: 2562 
Name: Find the Array Concatenation Value
Link: https://leetcode.com/problems/find-the-array-concatenation-value/description/
Solution Link: 
'''
# ====================================================


'''
Approach 1:  Successful
Paradigm: 
- Odd-even simple execution
No of Test Cases Passed: All
'''

'''
NOTES:
- 

MISTAKES:
- 

Time Complexity: O(N)
Space Complexity: O(1)
'''
# ====================================================
class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        l = len(nums)
        output = 0
        
        for i in range(l//2):
            output += int( str(nums[i]) + str(nums[-i-1]) )
            
        if len(nums)%2==1:
            output += nums[l//2]
        return output
        
