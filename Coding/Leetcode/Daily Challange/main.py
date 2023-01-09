'''
Leetcode Competition: Biweekly Contest
Date: January 7, 2023
Problem Number: 6289
Name: Find Xor-Beauty of Array
'''

'''
Approach 1:Failed, Brute Force
Approach 2: Successful, simple XOR
'''

class Solution:
    def xorBeauty(self, nums) -> int:
        ans = 0
        for i in nums:
            ans =  ans ^ i
            
        return ans
            
sol = Solution()
nums = [0,1]
res = sol.xorBeauty(nums)
print(f"res={res}")
