# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # refer the editorial stack solution
        # used two stacks for reverse both numbers
        s1=[]
        s2=[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        
        while l2:
            s2.append(l2.val)
            l2=l2.next
        ans=ListNode()
        total_sum=0
        while s1 or s2:
            if s1:
                total_sum+=(s1.pop())
            if s2:
                total_sum+=(s2.pop())

            ans.val=total_sum%10
            carry=total_sum//10
            head = ListNode(carry)
            head.next=ans
            ans=head
            total_sum=carry
        return ans.next if carry==0 else ans