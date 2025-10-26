# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        # Edge cases: empty list or single node
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length and last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Compute effective rotations
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find new tail (length - k - 1)th node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # Step 4: The node after new_tail is the new head
        new_head = new_tail.next
        
        # Step 5: Rotate the list
        new_tail.next = None
        tail.next = head
        
        return new_head
