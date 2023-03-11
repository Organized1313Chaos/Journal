class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        if self.next==None:
            return 'Empty'
        return str(self.val)

def list_to_linked_list(nums):
    if not nums:
        return None
    head = Node(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = Node(nums[i])
        curr = curr.next
    return head

# Driver Code
nums = [1, 2, 3, 4, 5]
head = list_to_linked_list(nums)

print(head)