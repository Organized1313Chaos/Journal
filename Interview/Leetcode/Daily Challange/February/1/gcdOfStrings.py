# ====================================================
'''
Leetcode Question
Date: February 11, 2023
Problem Number: 1071 
Name: Greatest Common Divisor of Strings
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach, Sliding Window
Paradigm: Sliding Window
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
Outer index was initially 0:N+1 --> Change it to 0:N

Time Complexity: 
Space Complexity:
'''
# ====================================================
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        out = ""
        n1 = len(str1)
        n2 = len(str2)

        for index in range(min(n1,n2)):
            if str1[index]==str2[index]:
                out += str1[index]
                continue
        if out=="": return out
        #case 1
        M = len(out)
        temp = out

        for p in range(M-1,-1,-1):
            out = temp[:p+1]
            flag = True
            N = len(out)
            for i in range(0, n1, N):
                if str1[i:i+N]!=out:
                    flag = False
                    break
                
            if flag==False:
                continue
            
            for i in range(0, n2, N):
                if str2[i:i+N]!=out:
                    flag = False
                    break
            if flag==False:
                continue
            
            return out

        return ""
        


# ====================================================

sol = Solution()
str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
res = sol.gcdOfStrings(str1, str2)
print(f"res={res}")
