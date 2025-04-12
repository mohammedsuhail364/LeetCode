# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=None
        if not head:
            return head
        while head:
            temp1=head.next
            head.next=temp
            temp=head
            head=temp1
        return temp

