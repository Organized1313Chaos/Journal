
'''
Leetcode Question
Date: January 11, 2023
Problem Number: 918
Name:  Maximum Sum Circular Subarray
'''

'''
# Brute Force
Approach 1: Partially Successful, Create all possible circular arrays and use kaden's algorithm 
Reason: Time Limit exceeded (TLE)
No of Test Cases Passed: 95/111
'''

'''
NOTES:
Time Complexity: O(N^2)
Space Complexity: O(N) --> To create a new array each time

MISTAKES:
Reason Of Failure: Not able to cover the edge cases.
'''


class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        N = len(nums)

        def helper(arr):
            sum_so_far = 0
            res = float('-inf')

            for num in arr:
                sum_so_far = max(num, num+sum_so_far)
                res =  max(res, sum_so_far)

            return res

        output = float('-inf')
        for i in range(0,  N):
            arr = nums[i:]+nums[:i]
            temp_ans = helper(arr)
            output = max(output,temp_ans )

        return output
    
sol = Solution()
nums =  [1,-2,3,-2]
res = sol.maxSubarraySumCircular(nums)
print(f"res={res}")

        