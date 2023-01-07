'''
Leetcode Competition: Biweekly Contest
Date: January 7, 2023

Problem Number: 6289
Name: Find Xor-Beauty of Array
'''

'''
Failed Approach 1: Brute Force
'''
class Solution:
    def xorBeauty(self, nums) -> int:
        triplets = []
        total = 0
        for i in nums:
            for j in nums:
                for k in nums:
                    triplets.append( (i,j,k) )
                    total = total ^  ((i | j) & k)
                    
        return total       
            
sol = Solution()
nums = [15,45,20,2,34,35,5,44,32,30]
res = sol.xorBeauty(nums)
print(f"res={res}")
