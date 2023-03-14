# ====================================================
'''
Leetcode Question
Date: March 13, 2023
Problem Number: 23
Name: Merge k Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach 
tags: Heapsort, Heap
No of Test Cases Passed: All
'''

'''
k --> len(lists)
N = max(list_elements)
Time Complexity: O(k*N*log(k*N)) 
Space Complexity: O(k*N*log(k*N))
'''
# ==============================================================================

# ==============================================================================
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        for lst in lists:
            while lst:
                heapq.heappush(heap,lst.val)
                lst = lst.next
        # res = []
        dummy = head = ListNode(0)
        while heap:
            ele = heapq.heappop(heap)
            node = ListNode(ele)
            head.next = node
            head = head.next
            # res.append(ele)

        return dummy.next

# =============================================================================
# ===============================APPROACH 2====================================
# Similar to merge sort
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(list1, list2):
            if not list1: return list2
            if not list2: return list1
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
        
        def merge_sort(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return arr[0]
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            left = merge_sort(left)
            right = merge_sort(right)
            return mergeTwoLists(left, right)

        return merge_sort(lists)
    
# ==============================APPROACH 3==================================
'''
Similar to traversing and merging two lists 
each time
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        
        def helper(l1,l2):
            if not l1: return l2
            if not l2: return l1
            
            curr = dummy = ListNode(0)
            
            while l1 and l2:
                if l1.val<l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1: dummy.next = l1
            if l2: dummy.next = l2
                
            return curr.next
        
        def helper2(lists):
            if len(lists)==0: return None
            if len(lists)==1: return lists[0]
            if len(lists)==2: return helper(lists[0],lists[1])
            
            mid = len(lists)//2
            return helper(lists[:mid+1],lists[mid+1:])
            
            
            
        if not lists: return None
        if len(lists)==1:
            return lists[0]
        res = lists[0]
        for i in range(1,len(lists)):
            res = helper(res,lists[i])
        return res 
    
# ==============================================================================
'''
MOST EFFICIENT ALGORITHM USING HEAP
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists)==1: return lists[0]

        import heapq
        heap = []
        head =  dummy = ListNode(0)
        for index, lst in enumerate(lists):
            if lst:
                heapq.heappush( heap, (lst.val, index) )
        
        while heap:
            val, index = heapq.heappop(heap)
            node = ListNode(val)
            head.next = node
            head = head.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush( heap, (lists[index].val, index) )

        return dummy.next


        
        

        




        