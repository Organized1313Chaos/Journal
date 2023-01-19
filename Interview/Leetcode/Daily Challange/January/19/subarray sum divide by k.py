
'''
Leetcode Question
Date: January 11, 2023
Problem Number: 974
Name: Subarray Sums Divisible by K
'''

'''
Approach 1: Partially Successful, Brute force approach. 
No of Test Cases Passed: 38/73
'''

'''
NOTES:
pass

MISTAKES:
Reason Of Failure: nums[i:j+1], earlier used--> nums[i:j]
j range--> If pairwise comparison is needed then we use i+1
       --> If all elements are needed, we need it from i 
'''

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        N = len( nums )
        output = 0
        for i in range(N):
            for j in range(i, N):
                if sum(nums[i:j+1])%k==0:
                    # print(nums[i:j+1])
                    output+=1
        
        return output
 
 
'''
Approach 2: Partially Successful, Brute force approach. 
No of Test Cases Passed: 66/73
'''

'''
NOTES:
- Use of prefix sum

MISTAKES:
pass
''' 
    
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        N = len( nums )
        output = 0
        for i in range(N):
            prefix = 0
            for j in range(i, N):
                prefix += nums[j]
                if prefix%k==0:
                    # print(nums[i:j+1])
                    output+=1
        
        return output

'''
Approach 3: Successful, Optimum approach using prefix sum 
No of Test Cases Passed: 73/73
'''

'''
NOTES:
- make sure initial remainder is 1 at 0

MISTAKES:
pass
''' 

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainders = [0]*k
        remainders[0] =1
        prefix = 0
        output = 0
        for  num in nums:
            prefix = ( prefix  + num%k +k) % k
            output +=  remainders[prefix]
            remainders[prefix] +=1
        
        return output
    
sol = Solution()
nums = [4,5,0,-2,-3,1]
k = 5
res = sol.subarraysDivByK(nums, k)
print(f"res={res}")

        
