'''
Leetcode Question
Date: February 13, 2023
Problem Number: 1523 
Name: Count Odd Numbers in an Interval Range
'''

'''
# Logical reasoning
Approach 1: Successful
No of Test Cases Passed: All
'''

'''
NOTES:
Time Complexity: O(1)
Space Complexity:O(1) 

MISTAKES:
Reason Of Failure: Not able to cover the edge cases.
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low_odd = True if low%2==1 else False
        high_odd = True if high%2==1 else False

        if low_odd and high_odd:
            return (high-low)//2 + 1
        if low_odd:
            return (high-low)//2 + 1
        if high_odd:
            return (high-low)//2 + 1
        return (high-low)//2