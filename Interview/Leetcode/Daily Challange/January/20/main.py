# ====================================================
# ====================================================
# ====================================================
'''
Leetcode Question
Date: January 20, 2023
Problem Number: 491 
Name: Non-decreasing Subsequences
'''
# ====================================================
# ====================================================
# ====================================================


'''
Approach 1: Failed Approach, Brute force 
- Sort based on values, and append the index if necessary 
No of Test Cases Passed: 8/58
'''

'''
NOTES:
pass

MISTAKES:
if you append a copy of list (mutable objects)
Ensure that you store a copy instead of reference
'''

# ====================================================

class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        N= len(nums)
        temp = []
        output = []
        
        for ind, val in enumerate(nums):
            temp.append((val, ind))
        
        temp.sort(key =  lambda x: (x[0], x[1]) )
        print(temp)
        print('\n'*2)
        
        result = []
        
        for i in range(N-1):
            if temp[i][0]==4:
                pass
            tp = [temp[i]]
            res_tp = [temp[i][0]]
            for j in range(i+1, N):
                if tp[-1][1]< temp[j][1]:
                    tp.append(temp[j])
                    res_tp.append( temp[j][0] )
                    output.append( tp )
                    result.append( res_tp.copy() )
                    
        return result

# ====================================================

'''
Approach 2: Heap Approach, heapify the tuple (value, index) 
- Did Not Implement

Approach 0: Monotonic Stack
Don't know if it will work
'''
# ====================================================


'''
Approach 3: Brute Force, Generate all the subsets
check if the subset is feasible to append
'''

'''
Note: If Solution space itself takes O(2^N) then may be your algorithm 
can run in exponential order
'''
# ====================================================

'''
Approach 4: Successful
Generate all the subsets that satisfy the given property
'''
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        subsets = [ [] ]
        
        for num in nums:
            temp  = subsets.copy()
            for lst in temp:
                ele = lst + [num]
                #DO not add if violets the conditino
                if len(ele)>1 and ele[-1] < ele[-2]:
                    continue   
                subsets.append(ele.copy())
            
        subsets  = [ tuple(lst) for lst in subsets if len(lst)>1 ]
        subsets = list( set(subsets) )

        return subsets
        

sol = Solution()
nums = [4,6,7,7]
res = sol.findSubsequences(nums)
print(f"res={res}")

        
