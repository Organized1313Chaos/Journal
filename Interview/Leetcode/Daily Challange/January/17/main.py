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
forgot to consider the initial case of increasing 1 as bit
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        dp = [0]*N

        num = 0
        if s[0]=='1': num+=1
        for ind, c in enumerate(s[1:], start=1):
            if c=='0':
                dp[ind] = min(dp[ind-1]+1, num) #previously sorted + flip 0-->1, flip all 1 to 0
            else:
                num+=1
                dp[ind] = dp[ind-1]
                
        print(dp)
        return dp[-1]