"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # this question is basically deep copy of all nodes but we dont know the random is where to point 
        # so we can create first all the nodes at start and map to each other with new nodes for random also
        cur = head
        oldToCopy = {None:None} # base case
        while cur:
            copy=Node(cur.val,cur)
            oldToCopy[cur]=copy
            cur=cur.next
        # now reassign the cur to the copy one and return head
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next
        return oldToCopy[head]