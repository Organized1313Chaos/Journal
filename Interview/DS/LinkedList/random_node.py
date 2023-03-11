
# ====================================================
'''
Leetcode Question
Date: March 11, 2023
Problem Number: 382 
Name: Linked List Random Node
Link: https://leetcode.com/problems/linked-list-random-node/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach 
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:

Time Complexity: O(1)
Space Complexity: O(1)
'''

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.lst = []
        if not head: return

        curr =head

        while curr:
            self.lst.append( curr.val )
            curr = curr.next

    def getRandom(self) -> int:
        import random
        return random.choice(self.lst)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()