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
        for i in nums:
            for j in nums:
                for k in nums:
                    triplets.append( (i,j,k) )
                    
        for p in triplets:
            for q in triplets:
                if ( (p[0]| p[1])&p[2] ) ^ ( (q[0]| q[1])&q[2] )==1:
                    print(f"{p} ^ {q} ==> {( (p[0]| p[1])&p[2] ) ^ ( (q[0]| q[1])&q[2] )}") 
            
sol = Solution()
nums = [0,1]
res = sol.xorBeauty(nums)
print(f"res={res}")
