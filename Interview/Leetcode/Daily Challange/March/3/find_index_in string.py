# ====================================================
'''
Leetcode Question
Date: March 4, 2023
Problem Number: 28
Name: Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach, Sliding Window
Paradigm: 
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
pass

Time Complexity: 
Space Complexity:
'''
# ====================================================

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):return -1
        l1 = len(needle)
        l2 = len(haystack)

        start = 0
        # A mistake here, 
        # I used l2-l1 instead of l2-l1+1
        while start<l2-l1+1:
            j = start
            while j<l2 and j-start<l1 and needle[j-start]==haystack[j]:
                j+=1
            
            if j-start==l1:
                return start
            
            start+=1

        return -1
    
# ====================================================

sol = Solution()
haystack = "sadbutsad"
needle = "sad"
res = sol.partition(haystack, needle)
print(f"res={res}")