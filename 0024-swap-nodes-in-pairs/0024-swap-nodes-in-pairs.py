# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # refer neetcode
        dummy=ListNode(0,head)
        prev=dummy
        cur = head
        while cur and cur.next:
            nxtPair = cur.next.next
            second = cur.next
            second.next = cur
            cur.next = nxtPair
            prev.next=second
            prev = cur
            cur = nxtPair
        return dummy.next