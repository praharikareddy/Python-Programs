# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast=head
        slow=head
        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            slow=slow.next
            if (fast==slow):
                break
        if(fast is None or fast.next is None):
            return None
        slow=head
        while(fast!=slow):
            slow=slow.next
            fast=fast.next
        return slow     