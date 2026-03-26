import unittest

# 1. 定義節點類別
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. 定義鏈結串列類別
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode(0)  # 虛擬頭節點，簡化邊界處理

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        # 優化：直接在初始化時指向原本的第一個節點
        new_node = ListNode(val, self.dummy_head.next)
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
        if index < 0:
            index = 0
            
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
        
        # 跳過要刪除的節點
        current.next = current.next.next
        self.size -= 1

# 3. 測試單元 (Unittest)
class TestMyLinkedList(unittest.TestCase):
    def setUp(self):
        self.obj = MyLinkedList()

    def test_basic_operations(self):
        """測試 LeetCode 官方範例流程"""
        self.obj.addAtHead(1)
        self.obj.addAtTail(3)
        self.obj.addAtIndex(1, 2)    # 串列變為 1->2->3
        self.assertEqual(self.obj.get(1), 2)
        
        self.obj.deleteAtIndex(1)    # 串列變為 1->3
        self.assertEqual(self.obj.get(1), 3)
        self.assertEqual(self.obj.size, 2)

    def test_edge_cases(self):
        """測試邊界情況"""
        # 空串列 get
        self.assertEqual(self.obj.get(0), -1)
        
        # 在索引 0 插入 (等同 addAtHead)
        self.obj.addAtIndex(0, 10)
        self.assertEqual(self.obj.get(0), 10)
        
        # 在末尾插入 (等同 addAtTail)
        self.obj.addAtIndex(1, 20)
        self.assertEqual(self.obj.get(1), 20)
        
        # 刪除唯一的節點
        self.obj.deleteAtIndex(0)
        self.obj.deleteAtIndex(0)
        self.assertEqual(self.obj.size, 0)

if __name__ == '__main__':
    # 執行測試
    unittest.main()