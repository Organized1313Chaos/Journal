'''
Leetcode Question
Date: January 11, 2023
Problem Number: 1443 
Name: Minimum Time to Collect All Apples in a Tree
'''

'''
Approach 1:Successful, Inorder Traversal
'''

'''
NOTES:
pass

MISTAKES:
pass
'''
class Solution:
    def countGood(self, nums, k) -> int:
        from collections import Counter
        N = len(nums)
        output = 0
        
        for i in range(N):
            for j in range(i+1, N):
                sub = nums[i:j+1]
                
                cn = Counter(sub)
                temp = 0
                
                for val in cn.values():
                    temp += val*(val-1)//2
                    if temp>k-1:
                        break
                if temp>k-1:
                    # print(nums[i:j+1])
                    output+=1
                    
        return output
                    
                
                
                
                
        return 0
        

sol = Solution()
nums = [3,1,4,3,2,2,4]
k = 2
res = sol.countGood(nums, k)
print(f"res={res}")

'''
p-m
a - o
r-s-k
e -i
'''
