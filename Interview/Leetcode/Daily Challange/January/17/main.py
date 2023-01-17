'''
Leetcode Question
Date: January 17, 2023
Problem Number: 926 
Name: Flip String to Monotone Increasing 
'''

'''
Approach 1:Successful, Two windows
Calculate all 0's to be flipped
two cases: if 0: decrease m and update ans
           else 1: increase m (why? To maintain left window with 0s, right window with 1s) 

Approach 2: Successful, dynamic programming
Link: https://leetcode.com/problems/flip-string-to-monotone-increasing/solutions/2912351/flip-string-to-monotone-increasing/
'''

'''
NOTES:

MISTAKES:
do not initialise ans as len(s)
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0

        for c in s:
            if c=='0':
                ans = min(ans+1, num)
            else:
                num +=1

        return ans