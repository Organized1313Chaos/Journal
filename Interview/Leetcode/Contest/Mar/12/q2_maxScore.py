# ====================================================
'''
Leetcode Contest Question
Date: March 13, 2023
Problem Number:  2587 
Name: Rearrange Array to Maximize Prefix Score
Link: https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/description/
Solution Link1 :
'''
# ====================================================

'''
Approach 1: Successful Approach, Greedy Approach 
Paradigm: Medium, Greedy
No of Test Cases Passed: All
'''

'''
NOTES:
- add all positives (Except zeros) to prefix sum
- decrease negative nums until the prefix sum is positive 

MISTAKES:
- if there are negative numbers and zeros then you should not add zeros

Time Complexity: O(N)
Space Complexity: O(N)
'''
# ====================================================
class Solution:
    def maxScore(self, nums: list[int]) -> int:
        positives = []
        negatives = []
        zeros = 0
        
        for num in nums:
            if num==0:
                zeros +=1 
                continue
            if num>0:
                positives.append(num)
            else:
                negatives.append(num)
        positives.sort()
        negatives.sort(reverse=True)
        
        # print(positives)
        # print(negatives)
        
        output = len(positives)
        if output>0:
            output += zeros
        prefix = sum(positives)
        
        for n in negatives:
            prefix+=n
            if prefix>0:
                output+=1
                continue
            break
    
        return output
        