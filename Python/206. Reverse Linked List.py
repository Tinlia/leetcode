# Runtime: 33ms | Beats 81.77% of submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        hold = None
        while curr is not None:
            hold = ListNode(curr.val, hold)
            curr = curr.next
        return hold
