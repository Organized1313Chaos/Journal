class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        if self.next==None:
            return 'Empty'
        return str(self.val)

def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

# =========================================

# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Convert the linked list to a list of numbers
res = linked_list_to_list(head)

# Print the result
print(res)  # Output: [1, 2, 3, 4, 5]
