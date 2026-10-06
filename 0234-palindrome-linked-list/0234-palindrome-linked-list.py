# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        total=0
        cur = head
        while cur:
            total+=1
            cur=cur.next
        # find the mid
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        second=prev
        first=head
        while first and second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True