# Bilding LinkedList data structure
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        if self.next==None:
            return 'Empty'
        return str(self.val)

def list_to_linked_list(nums, pos=None):
    if not nums:
        return None
    
    head = Node(nums[0])
    curr = head
    
    start = 0
    cycleNode = None
    for i in range(1, len(nums)):
        curr.next = Node(nums[i])
        if start == pos:
            cycleNode = curr
        curr = curr.next
        start +=1
    
    curr.next = cycleNode
    return head
# ======================================
node_list = [3,2,0,-4]
pos = 1
head = list_to_linked_list(node_list, pos)
# ======================================



# ====================================================
'''
Leetcode Question
Date: March 11, 2023
Problem Number: 142. 
Name: Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach 
Paradigm: Turtle and Hare Algoorithm, Floyed's cycle finding algorithm
No of Test Cases Passed: All
'''

'''
Time Complexity: O(N)
Space Complexity: O(N)
'''

'''
Mistakes:
slow != fast condition should not be in the main while loop
- You will be confused about when to stop 

- start the slow pointer from head to head.next
- start the fast pointer from head.next to head.next.next 

- Wrong: You don't have to check for slow==None and fast.next==None
- Correct: while fast and fast.next
'''

class Solution:
    def detectCycle(self, head: Node) -> Node:
        if not head or not head.next: return 
        
        slow = head
        fast = head.next

        while slow and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if fast!=slow: return 

        start = head

        while slow!=start:
            slow = slow.next
            start = start.next

        return slow
    
# ==========================================================================
s = Solution()
res = s.detectCycle(head)
print(f'res==>{res}')

# ============================================================
# correction in algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Node) -> Node:
        if not head or not head.next: return 
        
        slow = head.next
        fast = head.next.next

        while slow and fast.next and slow != fast:
            if slow==fast:
                break
            slow = slow.next
            fast = fast.next.next

        if not fast or not fast.next: return 

        start = head

        while slow!=start:
            slow = slow.next
            start = start.next

        return slow

        