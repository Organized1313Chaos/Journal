# ====================================================
'''
Leetcode Question
Date: January 27, 2023
Problem Number: 139 
Name: Word Break
Famous Name: "reachability" problem 
Link: https://leetcode.com/problems/word-break/description/
Official Solution: https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/
'''
# ====================================================

'''
Approach 1: Successful Approach, memoization and recursion
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:

Time Complexity: substrings O(N**3) 
Siza of recursion tree can grow upto N^2
Space Complexity: O(N)
The depth of recursion tree can grow upto O(N)
'''
# ====================================================
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        lookup = set(wordDict) 
        @lru_cache
        def helper(s):
            if s in lookup:
                return True
            
            for i in range(1, len(s)):
                if s[:i] in lookup:
                    if helper(s[i:]) == True:
                        return True
                    
            return False
                    
        
        return helper(s)
    
# ====================================================

sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
res = sol.findAllConcatenatedWordsInADict(s, wordDict)
print(f"res={res}")