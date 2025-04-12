# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # refer neetcode
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse it after the mid
        second=slow.next
        prev=None
        slow.next=None
        while second:
            tmp1=second.next
            second.next=prev
            prev=second
            second=tmp1
        # merge the two parts
        first,second=head,prev
        while first and second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        

