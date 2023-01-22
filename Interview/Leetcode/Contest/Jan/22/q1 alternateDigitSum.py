# ====================================================
'''
Leetcode Contest
Date: January 21, 2023
Problem Number: 2544
Name: Alternating Digit Sum
Link: https://leetcode.com/problems/alternating-digit-sum/description/
'''
# ====================================================

# ====================================================

'''
Approach 1: Successful Approach, Brute force 
- Sort based on values, and append the index if necessary 
No of Test Cases Passed: 8/58
'''

'''
NOTES:
- Don't forget to convert an integer to a string
- Check odd or even using a&1 instead of %(modulus) operator
MISTAKES:
'''

# ====================================================


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        result = 0
        cn = 1
        for num in n:
            result += int(num)*(cn)
            cn=cn*(-1)
            
        return result
            
        