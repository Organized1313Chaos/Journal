# ====================================================
'''
Leetcode Contest
Date: January 21, 2023
Problem Number: 2545 
Name: Sort the Students by Their Kth Score
Link: https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
'''
# ====================================================

# ====================================================

'''
Approach 1: Successful Approach, Sort using custom key function 
No of Test Cases Passed: All
'''

'''
NOTES:

MISTAKES:

'''

# ====================================================


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        result = sorted(score, key = lambda x : x[k], reverse = True)
        return result
        
        