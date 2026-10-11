# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        odd=ListNode()
        even=ListNode()
        oddTail ,evenTail = odd,even
        c=1
        while head:
            if c%2:
                oddTail.next=head
                oddTail=oddTail.next
            else:
                evenTail.next=head
                evenTail=evenTail.next
            head=head.next
            c+=1
        oddTail.next=even.next
        evenTail.next=None
        return odd.next