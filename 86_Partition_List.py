# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s_head = small = ListNode()
        l_head = large = ListNode()

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next

            head = head.next
    
        # Set the Last node of "large" list to NULL
        # The last node of "large" list might not be the last node of the original list like
        # [1 -> 4 -> 2], thus the node 4 would stll pointing to 2 form a cycle
        large.next = None
        small.next = l_head.next

        return s_head.next
        