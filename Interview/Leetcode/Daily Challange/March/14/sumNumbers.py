# ====================================================
'''
Leetcode Question
Date: March 14, 2023
Problem Number: 129
Name: Sum Root to Leaf Numbers
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful, Recursion 
Paradigm: 
tags: Binary Tree, Depth first Search
No of Test Cases Passed: All
'''

'''
NOTES:

MISTAKES:

Time Complexity: O(V)
Space Complexity: O(1) {instead of storing in a list, just store in a global variable} + O(|V|)
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = []
        def helper(root, string):
            if not root:
                return 

            if not root.left and not root.right:
                output.append(string + str(root.val))
            
            helper(root.left, string + str(root.val))
            helper(root.right, string + str(root.val))

        helper(root, "")
        output = list(map(int, output))

        return sum(output)