# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists or len(lists)==0:
            return None
        minHeap=[]
        for i,node in enumerate(lists):
            if node:
                heappush(minHeap,(node.val,i,node))
        dummy=ListNode()
        cur = dummy
        while minHeap:
            v,i,node = heappop(minHeap)
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(minHeap,(node.next.val,i,node.next))
        return dummy.next