# ====================================================
'''
Leetcode Question
Date: March 5, 2023
Problem Number: 2583
Name: Kth Largest Sum in a Binary Tree
Link: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach, DFS 
Paradigm: Using defaultdictionary to store sum 
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
- Missed minor detail to check,
- return kth largest, not kth level 

Time Complexity: O(nodes)
Space Complexity: O(levels), worst:O(N) [linear], average:O(log(N))
'''
# ====================================================





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        def helper(root, depth):
            if not root:
                return 
            lookup[depth] += root.val
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        
        helper(root, 1)
        
        res = lookup.values()
        res = sorted(res, reverse=True)
        if k<=len(res):
            return res[k-1]
        return -1
        