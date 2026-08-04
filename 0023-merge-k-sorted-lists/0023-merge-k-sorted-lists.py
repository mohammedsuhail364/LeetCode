# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            res=[]
            
            for i in range(0,len(lists),2):
                a=lists[i]
                b=lists[i+1] if i+1<len(lists) else None
                res.append(self.mergeTwoNodes(a,b))
            lists = res
        return lists[0]
    def mergeTwoNodes(self,a,b):
        node=ListNode()
        res=node
        while a and b:
            if a.val>b.val:
                node.next=b
                b=b.next
            else:
                node.next=a
                a=a.next
            node=node.next
        if a:
            node.next=a
        else:
            node.next=b
        return res.next