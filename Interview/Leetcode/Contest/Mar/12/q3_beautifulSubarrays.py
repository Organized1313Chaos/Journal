# ====================================================
'''
Leetcode Contest Question
Date: March 12, 2023
Problem Number: 2588.
Name: Count the Number of Beautiful Subarrays
Link: https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/description/
Solution Link1: https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/solutions/3286439/2588-solution-with-step-by-step-explanation/
Solution Link2: https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/solutions/3286771/python-3-o-n-tc-2588-count-the-number-of-beautiful-subarrays/

Observations:
Pattern1 : When we have to count arrays such that certain bitwise operations are performed
           use prefix array counts
Pattern 2: You had to check for 1's here, but by default xor automatically handles that
'''
# ===========================================================
# ====================Correct Solution=======================
class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        pre_xor = [0] * (n+1)
        pre_xor[0]=0
        cnt = [0]*(1<<20)
        cnt[0] = 1
        for i in range(1,n+1):
            pre_xor[i] = pre_xor[i-1] ^ nums[i-1]
            res += cnt[pre_xor[i]]
            cnt[pre_xor[i]] += 1

        return res
# ==============================================================================



'''
Approach 1: Partial Approach 
Paradigm: Bit Manipulations
Observation: if sum of 1 bits at index k is even, then it is beautiful subarray  
No of Test Cases Passed: 75/114
'''

'''
NOTES: 
pass

MISTAKES:
if you append a copy of list (mutable objects)
Ensure that you store a copy instead of reference

Time Complexity: O(N^2)
Space Complexity: O(bits(max(arr)))
'''
# ====================================================
class Solution:
    def beautifulSubarrays(self, numbers: list[int]) -> int:
        from collections import defaultdict, Counter
        
        def helper(nums):
            cn = Counter()
            index_lookup = defaultdict(int)

            for num in nums:
                bin_form = bin(num).lstrip('0b')
                # print(bin_form)
                bin_form = bin_form[::-1]
                for index, dig in enumerate(bin_form):
                    if dig=='0':
                        continue

                    index_lookup[index]+=1
                    
            #check if the whole sequence returns True
            for val in index_lookup.values():
                if val%2==1:
                    return False
            return True
        
        output = 0
        N = len(numbers)
        for i in range(N+1):
            for j in range(i+1, N+1):
                arr = numbers[i:j]
                if helper(arr)==True:
                    output +=1
        return output
        

# ===================Modification===========================================
'''
Mistake: (Silly) 
condition check failure: 
    Wrong: index_lookup[index]%2==0
    Right: index_lookup[index]%2==1
'''
'''
Improvement: 94/114
Testcases passed: 
'''
class Solution:
    def beautifulSubarrays(self, numbers: list[int]) -> int:
        from collections import defaultdict
        
        def helper(nums):
            output = 0
            index_lookup = defaultdict(int)

            for num in nums:
                bin_form = bin(num).lstrip('0b')
                # print(bin_form)
                bin_form = bin_form[::-1]
                flag = True
                for index, dig in enumerate(bin_form):
                    if dig=='0':
                        continue

                    index_lookup[index]+=1
                    if index_lookup[index]%2==1:
                        flag = False
                if flag==True:      
                    #check if the whole sequence returns True
                    for val in index_lookup.values():
                        if val%2==1:
                            flag = False
                            break
                if flag:
                    output +=1

            return output
        
        output = 0
        N = len(numbers)
        for i in range(N):
            arr = numbers[i:]
            print(arr)
            output += helper(arr)
        return output
# ==================================Merge Algo==================================
'''
Wrong Approach
Why?? 
let's say there is an array: [1,2,3,4,5]
we consider subarray: [1,2] and [3,4] but not [1,2,3]
Note:
So, whenever it is a question of subarrays, make sure if merge sort is the right algorithm to 
perform
'''
class Solution:
    def beautifulSubarrays(self, numbers: list[int]) -> int:
        from collections import defaultdict
        output = 0
        
        def helper_check(index_lookup):
            if not index_lookup:
                return 0
            for val in index_lookup.values():
                if val%2==1:
                    return 0
            return 1
                    
        
        def helper_merge(left, right, left_lookup, right_lookup):
            new_dict = {}
            for index, count in left_lookup.items():
                new_dict[index] = count 
                
            for index, count in right_lookup.items():
                if index in left_lookup:
                    new_dict[index]+=count
                else:
                    new_dict[index] = count
            return left+right, new_dict.copy()
        
        def helper(arr):
            nonlocal output
            index_lookup = defaultdict(int)
            if len(arr)==0:
                return arr, index_lookup
            
            if len(arr) == 1: 
                bin_form = bin(arr[0]).lstrip('0b')
                bin_form = bin_form[::-1]
                # print(arr[0])
                # print(bin_form)
                for index, dig in enumerate(bin_form):
                    if dig=='0':
                        continue

                    index_lookup[index]+=1
                print(f"output: {output}")
                output += helper_check(index_lookup)
                return arr, index_lookup    
                
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            left, left_lookup = helper(left)
            right, right_lookup = helper(right)
            res_arr, res_lookup = helper_merge(left, right, left_lookup, right_lookup)
            print(f"left: {left}, right: {right}")
            print(f"left_lookup: {dict(left_lookup)}, right_lookup: {dict(right_lookup)}")
            print(f"merged: {res_arr}, merger_lookup: {dict(res_lookup)}")

            output += helper_check(res_lookup)
            print(f"output: {output}")
            return res_arr, res_lookup

        N = len(numbers)
        
        helper(numbers)
        
        return output
    
# ==================================TESTCASES===================================
s= Solution()
nums = [4,3,1,2,4]
res = s.beautifulSubarrays(nums)
print(f"res ==> {res}")



























class Solution:
    def beautifulSubarrays(self, numbers: list[int]) -> int:
        from collections import defaultdict
        
#         def helper(nums):
#             cn = Counter()
#             index_lookup = defaultdict(int)

#             for num in nums:
#                 bin_form = bin(num).lstrip('0b')
#                 # print(bin_form)
#                 flag = True
#                 bin_form = bin_form[::-1]
#                 for index, dig in enumerate(bin_form):
#                     if dig=='0':
#                         continue

#                     index_lookup[index]+=1
#                     if index_lookup[index]%2==1:
#                         flag = False
#                 if flag==True:
#                     #check if the whole sequence returns True
#                     for val in index_lookup.values():
#                         if val%2==1:
#                             flag = False
#                             break
                
            
        return 0
        