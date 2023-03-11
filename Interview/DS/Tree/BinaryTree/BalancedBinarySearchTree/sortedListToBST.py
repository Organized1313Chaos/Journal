# ====================================================
'''
Leetcode Question
Date: March 11, 2023
Problem Number: 109 
Name: Convert Sorted List to Binary Search Tree
Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
Solution Link: 
'''
# ====================================================

# Main Solution
'''
Paradigm: Binary Search
'''

'''
Mistakes: 
- didn't add the condition: start>end
- In general we have to take floor index and recurse the other, but in this case
  we have to take math.ceil index 

'''


import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, lst):        
        N = len(lst)

        def helper(start, end):
            if start<0: return None
            if end>N-1: return None
            if start>end: return None
            
            if start == end:
                return TreeNode(lst[start])
            # odd length gives exact mid,
            # even length gives mid+1
            mid = math.ceil( (start + end)/2 )

            root = TreeNode(lst[mid])
            root.left =  helper(start, mid-1)
            root.right = helper(mid+1, end)

            return root

        tree = helper(0, N-1)
        return tree

# ======================================================
s = Solution()
lst = [-10,-3,0,5,9]
res = s.sortedListToBST(lst)
print(f"res-->{res}")