from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node  = ListNode()
        dummy = node
        
        while list1 and list2:
            # print(f"node-->{node.val}, dummy-->{dummy.val}, list1-->{list1.val}, list2-->{list2.val} ")
            if list1.val<=list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        while list1:
            # print(f"node-->{node.val}, dummy-->{dummy.val}, list1-->{list1.val}, list2-->{list2.val} ")
            node.next = ListNode(list1.val)
            list1 = list1.next
            node = node.next
        
        while list2:
            # print(f"node-->{node.val}, dummy-->{dummy.val}, list2-->{list2.val}")
            node.next = ListNode(list2.val)
            list2 = list2.next
            node = node.next

        return dummy.next



