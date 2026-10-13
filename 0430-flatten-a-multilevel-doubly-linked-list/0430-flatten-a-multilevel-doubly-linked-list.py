"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        # use a stack to store the next element
        cur=head
        stack=[]
        while cur or stack:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next=cur.child
                cur.child.prev = cur
                cur.child=None
            if not cur.next and stack:
                node = stack.pop()
                cur.next=node
                node.prev=cur
            cur=cur.next
        return head