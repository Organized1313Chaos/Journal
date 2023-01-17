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

'''

'''
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c=='0':
                m +=1
        
        ans = m

        for c in s:
            if c=='0':
                m-=1
                ans = min(m,ans)
            else:
                m+=1

        return ans
        
