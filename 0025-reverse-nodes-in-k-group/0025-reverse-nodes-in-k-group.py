# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def getKthNodeFn(node,k):
            cur = node
            while cur and k:
                cur=cur.next
                k-=1
            return cur
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            getKthNode = getKthNodeFn(groupPrev,k)
            if not getKthNode:break
            groupNext = getKthNode.next
            prev = getKthNode.next
            cur = groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = groupPrev.next
            groupPrev.next = getKthNode
            groupPrev = tmp

        return dummy.next
        
