# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums, head):
        nums=set(nums)
        cur=head
        res=ListNode()
        temp=res
        while cur:
            if cur.val not in nums:
                res.next=ListNode(cur.val)
                res=res.next
            cur=cur.next
        return temp.next
        
            
            