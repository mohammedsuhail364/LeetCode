# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        nums=[]
        while head:
            nums.append(head.val)
            head = head.next
        # split the array
        less=[]
        greater =[]
        for i in nums:
            if i<x:
                less.append(i)
            else:
                greater.append(i)
        head=ListNode()
        cur=head
        for x in less+greater:
            cur.next=ListNode(x)
            cur=cur.next
        return head.next