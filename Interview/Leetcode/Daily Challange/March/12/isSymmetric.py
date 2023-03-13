# ====================================================
'''
Leetcode Question
Date: March 13, 2023
Problem Number: 101 
Name: Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach
Paradigm: Tree, Easy, Mirroring 
No of Test Cases Passed: All
'''

'''

Time Complexity: O(|V|)
Space Complexity: O(|V|)  [size of a stack]
'''
# ====================================================

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if root:
            if not root.left and not root.right:
                return True
            if not root.left:
                return False
            if not root.right:
                return False
            
        
        def mirror(left, right):
            if not left and not right:
                return True
            if left and not right:
                return False
            if not left and right:
                return False
            if left.val != right.val:
                return False

            return mirror(left.left, right.right) and mirror(left.right, right.left) 
        
        return mirror(root.left, root.right)
