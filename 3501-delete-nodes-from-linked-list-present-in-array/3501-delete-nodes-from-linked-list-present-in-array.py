# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums, head):
        nums=set(nums)
        res=ListNode(0,head)
        prev=res
        
        while head:
            if head.val in nums:
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return res.next
        
            
            