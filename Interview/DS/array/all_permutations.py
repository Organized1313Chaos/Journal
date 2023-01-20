'''
Reference: https://leetcode.com/problems/subsets/solutions/464411/subsets/
'''

# Approach 1: Recursive Algorithm
# ==========================================================================
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums)==1:
            return [nums]

        res = []

        for i in range(len(nums)):
            temp_permute =  self.permute(nums[:i]+nums[i+1:])
            for j in temp_permute:
                res += [ [nums[i]]+j]

        return res
    

# Approach 2: Built In Tools
# ==========================================================================
import itertools

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return itertools.permutations(nums)
    
# ==========================================================================
# Approach 3: Backtracking and Swapping

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        def back_track(nums, p):
            if p == len(nums) - 1:
                ans.append(nums[:])
                return
            for i in range(p, len(nums)):
                nums[i], nums[p] = nums[p], nums[i]
                back_track(nums, p + 1)
                nums[i], nums[p] = nums[p], nums[i]
            return

        ans = []; back_track(nums, 0)
        return ans
# ==========================================================================
