# ====================================================
'''
Leetcode Question
Date: March 5, 2023
Problem Number: 2585 
Name: Number of Ways to Earn Points
Link: https://leetcode.com/problems/number-of-ways-to-earn-points/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Partially Successful Approach, Recursion
Paradigm: Recursion, DP
- 
No of Test Cases Passed: 9/60
'''

'''
NOTES:
pass

MISTAKES:
- LRU Cache implementaton Failed

Time Complexity: 
Space Complexity:
'''
# ====================================================
class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        # @lru_cache
        def helper(n, t_sum):
            #Base case
            if t_sum == 0:
                return 1

            if t_sum<0:
                return 0

            if n<=0:
                return 0

            #exclude
            case1 = helper(n-1, t_sum)
            #include
            if types[n-1][0]<0:
                return 0

            reduction = types[n-1][1]
            types[n-1][0] -= 1
            case2 =  helper(n, t_sum - reduction)
            types[n-1][0] += 1

            return case1+ case2

        n = len(types)
        res = helper(n, target)

        return res
    

sol = Solution()
target = 6
types = [[6,1],[3,2],[2,3]]
res = sol.waysToReachTarget(target, types)
print(f"res={res}")

# =======================================================
'''
LRU_Cache updation
'''
from functools import lru_cache
class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        @lru_cache
        def helper(n, t_sum, left, price):
            #Base case
            if t_sum == 0:
                return 1

            if t_sum<0:
                return 0

            if n<=0:
                return 0

            #exclude
            case1 = helper(n-1, t_sum, types[n-2][0],  types[n-2][1])
            #include
            if types[n-1][0]<0:
                return 0

            reduction = types[n-1][1]
            types[n-1][0] -= 1
            case2 =  helper(n, t_sum - reduction, types[n-1][0], types[n-1][1])
            types[n-1][0] += 1

            return case1+ case2

        n = len(types)
        res = helper(n, target, types[n-1][0],  types[n-1][1])

        return res
    
# =====================================================================================
'''
Solution Link: 
'''
from functools import cache
class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        @cache
        def dfs(i, target):
            if target == 0: return 1
            if i >= len(types) or target < 0: return 0
            return sum(dfs(i + 1, target - j * types[i][1]) for j in range(types[i][0] + 1)) % 1000000007
        return dfs(0, target)