from functools import lru_cahce

# ====================================================
'''
Leetcode Question
Date: January 30, 2023
Problem Number: 1137 
Name: N-th Tribonacci Number
Link: https://leetcode.com/problems/n-th-tribonacci-number/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach, recusrion and memoization
Paradigm: Dynamic Programming, Recursion

No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
pass

Time Complexity: recursion calls O(N)
Space Complexity: O(N), built-in recursion stack

'''
# ====================================================

class Solution:
    # @lru_cache
    def tribonacci(self, n: int) -> int:
        if n in (1,2): return 1
        if n==0: return 0

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) 