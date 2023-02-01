# ====================================================
'''
Leetcode Question
Date: February 11, 2023
Problem Number: 1071 
Name: Greatest Common Divisor of Strings
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
Solution Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3024822/greatest-common-divisor-of-strings/?orderBy=most_votes
'''
# ====================================================

'''
Approach 1: Successful Approach, Sliding Window
Paradigm: Sliding Window
No of Test Cases Passed: All
'''

'''
NOTES:
- Since both strings contains multiples of the identical segment base, their concatenation must be consistent, regardless of the order (str1 + str2 = str2 + str1).

MISTAKES:
- Outer index was initially 0:N+1 --> Change it to 0:N
- Condition:
    if n2%N!=0 or n1%N!=0:
        continue
- Failed TestCase:
  "AAACCC", "AAA"
- imporovement: try ( candidate_string*(N//n)==originalstring )

Time Complexity: O(min(m,n)⋅(m+n)) 
Space Complexity:

Official solution:
Time complexity: O(m+n)O(m + n)O(m+n)
'''
# ====================================================        
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        # n1 is small
        if n1>n2:
            str1, str2 = str2, str1
            n1, n2 = n2, n1
            
        for p in range(n1-1, -1, -1):
            out = str1[:p+1]
            N = len(out)
            flag = True
            
            if n2%N!=0 or n1%N!=0:
                continue

            for i in range(0, n1, N):
                main_string = str2[i:i+N] 
                if str1[i:i+N]!=out:
                    flag = False
                    break
            if flag == False:
                continue
            
            for i in range(0, n2, N):
                main_string = str2[i:i+N] 
                if str2[i:i+N]!=out:
                    flag = False
                    break
            if flag == False:
                continue
                
            if flag: return out
            
        return ""
# ====================================================

sol = Solution()
str1 = "NLZGMNLZGM NLZGMNLZGMNLZGM NLZGMNLZGMNLZGM"
str2 = "NLZGMNLZGM NLZGMNLZGMNLZGM NLZGMNLZGMNLZGM NLZGM"
str1 = "".join(str1.split())
str2 = "".join(str2.split())
res = sol.gcdOfStrings(str1, str2)
print(f"res={res}")

# ======================================================
# Observations Dude, Observations!!!!!!!!!
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2 != str2 + str1):
            return ""
        return str1[:math.gcd(len(str1),len(str2))]