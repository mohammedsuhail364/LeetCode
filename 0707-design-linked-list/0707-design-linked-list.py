class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
class MyLinkedList:

    def __init__(self):
        self.head=None
    def get(self, index: int) -> int:
        i=0
        cur=self.head
        while cur:
            if i==index:
                return cur.val
            cur=cur.next
            i+=1
        return -1
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next=self.head
        self.head=node
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        cur=self.head
        while cur.next:
            cur = cur.next
        cur.next=Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        i=0
        cur=self.head
        while cur:
            if i==index-1:
                node=Node(val)
                node.next = cur.next
                cur.next=node
                return
            cur=cur.next
            i+=1
    def deleteAtIndex(self, index: int) -> None:
        i=0
        if index==0:
            self.head=self.head.next
            return
        cur=self.head
        while cur:
            if i == index - 1:
                if cur.next is None:  # index out of bounds
                    return
                cur.next = cur.next.next  # actually relinks the list
                return
            cur=cur.next
            i+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)