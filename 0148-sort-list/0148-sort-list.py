# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # refer neetcode
        # this question is basically a combination of the find mid values in the linked list and merge two sorted list
        # uses the same for recurrsion 
        if not head or not head.next:
            return head
        left = head
        mid = self.getMid(head)
        right = mid.next 
        mid.next=None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeSortedList(left,right)
    def getMid(self,head):
        # using the floyd's algorithm to find the mid 
        slow = head
        fast = head.next # this is because we need find the mid we use only head means it gives after the mid node
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeSortedList(self,left,right):
        dummy = ListNode()
        res=dummy
        while left and right:
            if left.val<=right.val:
                res.next=left
                left=left.next
            else:
                res.next=right
                right = right.next
            res=res.next
        if left:
            res.next=left
        if right:
            res.next=right
        return dummy.next
