'''
Reference: https://leetcode.com/problems/subsets/solutions/464411/subsets/
'''

# Approach 1: Cascading
# ==========================================================================
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
    
    

# Approach 2: Backtracking
# ==========================================================================

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
# ==========================================================================
# Approach 3: Lexicographic (Binary Sorted) Subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output
# ==========================================================================


class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        result = set()
        sequence = []

        def backtrack(index):
            # if we have checked all elements
            if index == len(nums):
                result.add(tuple(sequence))
                return
            # if the sequence remains increasing after appending nums[index]
            
            # append nums[index] to the sequence
            sequence.append(nums[index])
            # call recursively
            backtrack(index + 1)
            # delete nums[index] from the end of the sequence
            sequence.pop()
            # call recursively not appending an element
            backtrack(index + 1)
        
        backtrack(0)
        return result