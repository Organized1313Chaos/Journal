## Kaden's algorithm

class Solution:
    def maxSubArray(self, nums) -> int:
        sum_so_far = 0
        res = float('-inf')

        for num in nums:
            sum_so_far = max(num, num+sum_so_far)
            res =  max(res, sum_so_far)

        return res
    
s = Solution()
testcase =  [-2,1,-3,4,-1,2,1,-5,4]
res = s.maxSubArray(testcase)

print(f"res==>{res}")