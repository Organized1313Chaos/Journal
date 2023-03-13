# ====================================================
'''
Leetcode Question
Date: January 11, 2023
Problem Number: 974
Name: Subarray Sums Divisible by K
Link: 
Solution Link: 
'''
# ====================================================

'''
Approach 1: Failed Approach, Brute force 
Paradigm: 
tags: 
- Sort based on values, and append the index if necessary 
No of Test Cases Passed: 8/58
'''

'''
NOTES:
pass

MISTAKES:
if you append a copy of list (mutable objects)
Ensure that you store a copy instead of reference

Time Complexity: 
Space Complexity:
'''
# ====================================================
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        N = len(s)

        def isPalindrome(string):
            if len(string)<2: return True
            l, r = 0, len(string)-1

            while l<r:
                if string[l]!=string[r]:
                    return False
                
                l+=1
                r-=1
            
            return True

        output = []

        def helper(i, string, path=[]):
            nonlocal output
            if i==N:
                output.append(path)
                return
            
            if isPalindrome(string):
                path.append(string)
                output.append(path)
                path.pop(-1)
            
            for j in range(1, len(string)):
                str1 = string[:j]
                str2 = string[j:]
                if isPalindrome(str1):
                    path.append(str1)
                    helper(0, str2, path)

        helper(0,s,[])
        pass
# ====================================================

sol = Solution()
s = "aab"
res = sol.partition(s)
print(f"res={res}")

        
