class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        # noew_node -> [1]
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

        self.size += 1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head
        for _ in range(index):
            cur = cur.next
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None

# class MyLinkedList(object):
#     def __init__(self):
#         # 建立虛擬節點 (Sentinel Nodes)
#         self.head = Node(None)
#         self.tail = Node(None)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.size = 0

#     def get(self, index):
#         """
#         :type index: int
#         :rtype: int
#         """

#         if index < 0 or index >= self.size:
#             return -1
    
#         curr = self.head 
        
#         for _ in range(index):
#             curr = curr.next
            
#         return curr.val

# --- 測試執行區塊 ---
if __name__ == "__main__":
    obj = MyLinkedList()
    
    # 為了測試 get，我們手動模擬插入兩個節點 (值分別為 100 和 200)
    # 結構：head <-> node1(100) <-> node2(200) <-> tail
    node1 = Node(100)
    node2 = Node(200)
    
    # 手動連結指針
    obj.head.next = node1
    node1.prev = obj.head
    node1.next = node2
    node2.prev = node1
    node2.next = obj.tail
    obj.tail.prev = node2
    obj.size = 2 # 設定長度為 2
    
    # 測試開始
    print(f"測試 index 0 (預期 100): {obj.get(0)}")
    print(f"測試 index 1 (預期 200): {obj.get(1)}")
    print(f"測試 index 2 (預期 -1): {obj.get(2)}")
    print(f"測試 index -1 (預期 -1): {obj.get(-1)}")
