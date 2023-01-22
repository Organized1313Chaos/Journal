# ====================================================
'''
Leetcode Contest
Date: January 21, 2023
Problem Number: 2547
Name: Minimum Cost to Split an Array
Link: https://leetcode.com/problems/minimum-cost-to-split-an-array/description/
'''
# ====================================================

# ====================================================
'''
Approach 1 Failure, Didn't Try
'''

'''
NOTES:

MISTAKES:
'''

# ====================================================
from collections import defaultdict
class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        dp=[0]
        nums=[-1]+nums
        def main(i):
            mp=defaultdict(int)
            s=0
            ans=10000000000000
            while i>0:
                if mp[nums[i]]>0:
                    s+=1
                    if mp[nums[i]]==1:
                        s+=1
                mp[nums[i]]+=1
                ans=min(dp[i-1]+s,ans)
                i-=1
            return ans+k
                
            
        for i in range(1,len(nums)):
            dp.append(main(i))
        return dp[-1]
            
        