# Calculate
# hours*k<=sum(arr)
# arr[i] <= k
# range of k<=max(arr)

# ====================================================
'''
Leetcode Question
Date: March 8, 2023
Problem Number: 875
Name: Koko Eating Bananas
Link: https://leetcode.com/problems/koko-eating-bananas/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach 
Paradigm: Binary Search
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:

Time Complexity: O(log(N))
Space Complexity: O(log(N))
'''
# ====================================================

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        import math
        if len(piles)==h: return max(piles)
        N = len(piles)
        def helper(k):
            # k --> cookies to be eaten
            # with the given time
            curr = 0
            for p in piles:
                curr = curr + math.ceil(p/k)
            if curr>h:
                return False
            return True
                
        lo = 1
        hi = max(piles)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if not helper(mid): lo = mid + 1
            else: hi = mid
        return lo

            
        
# =============================================================

sol = Solution()
piles = [3,6,7,11]
h = 8
res = sol.minEatingSpeed(piles, h)
print(f"res={res}")