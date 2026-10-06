# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # refer neetcode
        # find the mid way point
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second = slow.next
        slow.next=None
        # reverse the second half
        prev=None
        while second:
            tmp = second.next
            second.next=prev
            prev=second
            second = tmp
        # merge the two halves
        first = head
        second = prev
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first=tmp1
            second=tmp2
