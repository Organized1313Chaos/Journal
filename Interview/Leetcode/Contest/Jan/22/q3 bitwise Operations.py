# ====================================================
'''
Leetcode Contest
Date: January 21, 2023
Problem Number: 2546 
Name: Apply Bitwise Operations to Make Strings Equal
Link: https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/
'''
# ====================================================
# ====================================================

'''
Approach 1 Failure, Brute force 
'''

'''
NOTES:
- Whenever you have to deal with two indices simultaneously
- Consider the case of two bits, four possibilities

MISTAKES:
'''

# ====================================================

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ( '0'*len(s) not in (s, target) ) or (s==target)
            
        