# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)

        less_list = less_head
        greater_list = greater_head

        current = head

        while current:
            if current.val < x:
                less_list.next = current
                less_list = less_list.next
            else:
                greater_list.next = current
                greater_list = greater_list.next
            current = current.next
        
        greater_head.next = None
        less_list.next = greater_head

        return less_head.next