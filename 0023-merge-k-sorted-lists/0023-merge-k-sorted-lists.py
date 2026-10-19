# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        minHeap = []
        for i,node in enumerate(lists):
            if node:
                heappush(minHeap,(node.val,i,node))
        dummy = ListNode()
        res = dummy
        while minHeap:
            val,idx,node = heappop(minHeap)
            res.next = node
            res=res.next
            if node.next:
                heappush(minHeap,(node.next.val,idx,node.next))
        return dummy.next