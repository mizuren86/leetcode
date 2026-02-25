class LinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.dummy_head.next)
        # point to node head
        new_node.next = self.dummy_head.next
        # renew head with new_node
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        
        current = self.dummy_head
        for _ in range(index):
            current = current.next
        
        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.dummy_head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

