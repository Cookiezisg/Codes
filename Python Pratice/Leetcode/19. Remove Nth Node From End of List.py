# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        # Return the head of the new list
        return dummy.next