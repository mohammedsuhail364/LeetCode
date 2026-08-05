# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        min_heap=[] # min heap
        for i,l in enumerate(lists):
            if l:
                heappush(min_heap,(l.val,i,l))
        dummy=ListNode(0)
        cur=dummy
        while min_heap:
            val,i,node = heappop(min_heap)
            cur.next=node
            cur=cur.next
            if node.next:
                heappush(min_heap,(node.next.val,i,node.next))
        return dummy.next
