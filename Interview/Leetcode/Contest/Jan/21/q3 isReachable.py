# ====================================================
'''
Leetcode Contest
Date: January 21, 2023
Problem Number: 2543 
Name:  Check if Point Is Reachable
Link: https://leetcode.com/problems/check-if-point-is-reachable/description/
'''
# ====================================================

# ====================================================
'''
Approach 1: Half Approach, Linear Transformation Approach
Solution Link: https://leetcode.com/problems/check-if-point-is-reachable/solutions/3082073/java-c-python-1-line-gcd-solution/
'''

'''
NOTES:

MISTAKES:
'''
# ====================================================

class Solution:
    def isReachable(self, x: int, y: int) -> bool:
        import math
        while x%2==0:
            x = x>>1
            
        while y%2==0:
            y = y>>1
            
        return math.gcd(x,y)==1
            
            
        

