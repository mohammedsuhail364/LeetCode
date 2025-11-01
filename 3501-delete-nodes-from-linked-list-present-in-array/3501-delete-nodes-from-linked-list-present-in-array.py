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
        cur=head
        while cur:
            if cur.val in nums:
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next
        return res.next
        
            
            