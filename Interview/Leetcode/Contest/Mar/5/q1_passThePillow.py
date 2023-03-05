# ====================================================
'''
Leetcode Question
Date: March 5, 2023
Problem Number: 2582 
Name: Pass the Pillow
Link: https://leetcode.com/problems/pass-the-pillow/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach 
Paradigm: Detailed Analysis 
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
- modulo (n-1) instead of (n)
- cycles (2*(n-1)) 
- Devide the approach with the cases, 0 time, first cycle, second cycle

Time Complexity: O(1)
Space Complexity: O(1), worst:O(1) [Constant Space Time], average:O(1)
'''
# ====================================================

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Calculate the number of full cycles
        num_cycles = time // (2 * (n - 1))
        # Calculate the remaining time after full cycles
        remaining_time = time % (2 * (n - 1))
        # Calculate the final position of the pillow
        if remaining_time == 0:
            position = 1
            return position
        elif remaining_time <= n - 1:
            position = 1 + remaining_time
            return position
        # else:
        #     remaining_time = remaining_time - (n-1)
        #     position = n - remaining_time
            
        #     return position










        