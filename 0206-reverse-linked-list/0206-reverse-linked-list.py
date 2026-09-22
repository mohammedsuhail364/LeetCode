# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        prev=None
        cur=head
        while cur:
            nxt=cur.next 
            cur.next=prev 
            prev=cur
            cur=nxt
        return prev
