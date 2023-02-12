# ====================================================
'''
Leetcode Question
Date: February 12, 2023
Problem Number: 2564
Name:  Substring XOR Queries
Link: https://leetcode.com/problems/substring-xor-queries/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Failed Approach, Brute force 
Paradigm: Inverse of Xor is XOR itself
No of Test Cases Passed: 54/59 TLE
'''

'''
NOTES:
- Could not execute it properly

MISTAKES:
pass

Time Complexity: O(N^2+ q)
Space Complexity: O(N^2)
'''
# ====================================================

class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        self.lookup = {}
        l= len(s)
        for i in range(l):
            for j in range(i,l):
                bit = s[i:j+1]
                if bit not in self.lookup:
                    self.lookup[bit] = [i,j]
        
        # print(self.lookup)
        output = []
        for q in queries:
            start, end = q
            ans = start^end
            ans = bin(ans).replace("0b","")
            if ans in self.lookup:
                output.append(self.lookup[ans])
            else:
                output.append( [-1,-1] )
            
        return output
        
            
sol = Solution()
nums = [1,7,9,2,5]
lower = 11
upper = 11
res = sol.countFairPairs(nums, lower, upper)
print(f"res={res}")


# =================================================================
'''
Solution similar to mine
'''
from functools import lru_cache

class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        return [self.solve(s, q[0] ^ q[1]) for q in queries]
    
    @lru_cache(maxsize=None)
    def solve(self, s, val):
        val_str = "{0:b}".format(val)
        idx = s.find(val_str)
        sol = [idx, idx + len(val_str) - 1] if idx >= 0 else [-1, -1]
        return sol
    
# ======================================================================================
'''
The solution below works though
'''

class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        ans = []
        cache = dict()
        for q in queries:
            val = q[0] ^ q[1]
            if val in cache:
                ans.append(cache[val])
                continue
            val_str = "{0:b}".format(val)
            idx = s.find(val_str)
            if idx >= 0:
                sol = [idx, idx + len(val_str) - 1]
            else:
                sol = [-1, -1]
            ans.append(sol)
            cache[val] = sol
        return ans

        
        
        
        
        