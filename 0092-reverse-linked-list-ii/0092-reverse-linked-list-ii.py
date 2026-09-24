# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # refer neetcode
        dummy = ListNode(0,head)
        leftPrev=dummy
        cur=head
        for i in range(left-1):
            leftPrev=cur
            cur=cur.next
        # reverse the linked list 
        prev=None 
        for i in range(right-left+1):
            tmp = cur.next
            cur.next = prev
            prev=cur
            cur=tmp
        # update the left and right pointers
        leftPrev.next.next=cur
        leftPrev.next=prev
        return dummy.next