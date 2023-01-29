'''
Leetcode Weekly Contest
Date: January 29, 2023
Problem Number: 974
Name: Subarray Sums Divisible by K
Link: https://leetcode.com/problems/count-distinct-numbers-on-board/description/
Solution Link: None
'''
# ====================================================

'''
Approach 1: Successful Approach, 
Paradigm: Loop Iteration, Maths
- Maintain a set with already traversed numbers
No of Test Cases Passed: All
'''

'''
NOTES:
INstead of stack you could have used set somehow

MISTAKES:

Time Complexity: O(N)
Space Complexity: O(N)
'''
# ====================================================

class Solution:
    def distinctIntegers(self, n: int) -> int:
        stack = [n]
        lookup = set()
        count = 0
        while stack:
            num = stack.pop(-1)
            if num in lookup: continue
            lookup.add(num)
            count+=1
            for i in range(2,num):
                if i not in lookup and num%i==1:
                    stack.append(i)
                    
        return count
    

sol = Solution()
s = 5
res = sol.distinctIntegers(s)
print(f"res={res}")

# ======================================================
'''
Observation:
for each N, N%(N-1)==1
So, we will have, N, N-1, N-2, N-3 etc a series
And hence ans will be from N-1 except for 1 (1 divides every number)
'''

class Solution:
    def distinctIntegers(self, n: int) -> int:
        return max(1, n-1)