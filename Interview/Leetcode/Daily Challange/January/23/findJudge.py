# ====================================================
'''
Leetcode Question
Date: January 23, 2023
Problem Number: 997
Name: Find the Town Judge
Link: https://leetcode.com/problems/find-the-town-judge/description/
'''
# ====================================================

'''
Approach 1: Successful Approach 
- Mark the person who trusts as not judge,
- The judge needs the support of everyone

Approach 2: 
Trusted_to == 0 and Trsted_by == n-1
No of Test Cases Passed: 100/100
'''

'''
NOTES:
pass

MISTAKES:
Property 2 was not so clear.
'''

# =======================================================
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        cross = [True]*(n+1)
        judge = [0]*(n+1)
        judge[0] = n-1
        cross[0] = False

        for p1, p2 in trust:
            judge[p2] += 1
            cross[p1] = False 

        for ind, val in enumerate(cross):
            if val==True and judge[ind]==n-1:
                return ind

        return -1