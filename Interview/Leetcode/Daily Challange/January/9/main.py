'''
Leetcode Question
Date: January 9, 2023
Problem Number: 239
Name: Sliding Window Maximum
'''

'''
Approach 1:Failed, Brute Force
'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        N = len(nums)
        for i in range(N-k+1):
            new_arr = nums[i:i+k]
            new_mx = max(new_arr)
            output.append( new_mx )
            
        return output
               
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = sol.maxSlidingWindow(nums, k)
print(f"res={res}")
