# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if not head:
            return None
        cur=head
        prev=None
        while cur:
            if cur.val==val:
                if not prev:
                    head=head.next
                    cur=head
                else:
                    prev.next=cur.next
                    cur=cur.next

            else:
                prev=cur
                cur=cur.next
        return head