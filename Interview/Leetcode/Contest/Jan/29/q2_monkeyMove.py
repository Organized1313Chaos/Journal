# Test Cases Passed: ALL

# ====================================================
'''
Leetcode Weekly Contest
Date: January 29, 2023
Problem Number: 2550 
Name: Count Collisions of Monkeys on a Polygon
Link: https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
Solution Link: https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/solutions/3111623/very-clear-explanation-straightforward-solution/
'''
# ====================================================

'''
Approach 1: Successful Combinatorics
Total Possible Outcomes: 2^n
Not possible outcomes: 2 (Clockwise and anti-clockwise)

No of Test Cases Passed: All
'''

'''
NOTES:
-  Calculating powers for large numbers

MISTAKES:
- Forgot to include modulus operations

Time Complexity: O(1) --> Pure Math, O(logN)
Space Complexity:O(1)
'''

class Solution:
    def monkeyMove(self, n: int) -> int:
        modulo = 1_000_000_007
        power = 1
        exponent = 2
        while n:
            if n&1:
                power *= exponent                
            exponent = (exponent*exponent) % modulo
            n >>= 1
        answer = power        
        answer += modulo - 2
        answer %= modulo      
        return answer
