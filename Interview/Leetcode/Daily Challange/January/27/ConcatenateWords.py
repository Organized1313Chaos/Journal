# ====================================================
'''
Leetcode Question
Date: January 27, 2023
Problem Number: 472 
Name: Concatenated Words
Link: https://leetcode.com/problems/concatenated-words/description/
Solution: https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/
'''
# ====================================================
'''
Approach 1: Successful Approach, memoization and recursion (Brute Force)
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
pass

M - Length of longest string
N - Length of the word List
Time Complexity: O(M^3 * N)  [dp approach ]

 we need to consider the cost to calculate the hash value of a string internally which would be O(M)O(M)O(M).

Space Complexity: O(N. M)
The depth of recursion tree can grow upto O(N)
'''
# ====================================================

from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        N = len(words)
        lookup = set(words)
        
        # @lru_cache
        def helper(s):
            if s in lookup:
                return True
            
            for i in range(1, len(s)):
                if s[:i] in lookup:
                    if helper(s[i:]) == True:
                        return True
                    
            return False
        
        output = []
        for s in words:
            lookup.remove(s)
            if helper(s)==True:
                output.append( s )
            lookup.add(s)
            
        return output
    

sol = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
res = sol.findAllConcatenatedWordsInADict(words)
print(f"res={res}")


# ==============================================================================



'''
Approach 2: Successful Approach, dp
No of Test Cases Passed: All
'''
'''

NOTES:
pass

MISTAKES:
pass

M - Length of longest string
N - Length of the word List
Time Complexity: O(M^3 * N)  [dp approach ]
Space Complexity: O(N. M)
The depth of recursion tree can grow upto O(N)
'''
# ====================================================

from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        answer = []
        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            for i in range(1, length+1):
                for j in range(i-1, -1, -1):
                    if dp[j] and word[j:i] in dictionary:
                        dp[i] = True
                        break
            if dp[length]:
                answer.append(word)
        return answer
