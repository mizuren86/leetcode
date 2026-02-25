from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next

    def removeElement(self, nums: List[int], val: int) -> int:
        i, size = 0, len(nums)
        while i < size:
            if nums[i] == val:
                for j in range(i+1, l):
                    nums[j-1] = nums[j]
                i -= 1
                size -= 1
            i += 1
        return size
    
    # two pointer
    def removeElement1(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        

    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head

    def linked_list_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

# test cases
ts = Solution()

# case 1
nums1 = [1, 2, 6, 3, 4, 5, 6]
val1 = 6
list1 = create_linked_list(nums1)
result1_head = ts.removeElements(list1, val1)
result1 = linked_list_to_list(result1_head)
expected1 = [1, 2, 3, 4, 5]
print(f"Input: head = {nums1}, val = {val1}, Output: {result1}, Expected: {expected1}, Match: {result1 == expected1}")

# case 2
nums2 = []
val2 = 1
list2 = create_linked_list(nums2)
result2_head = ts.removeElements(list2, val2)
result2 = linked_list_to_list(result2_head)
expected2 = []
print(f"Input: head = {nums2}, val = {val2}, Output: {result2}, Expected: {expected2}, Match: {result2 == expected2}")

# case 3
nums3 = [7, 7, 7, 7]
val3 = 7
list3 = create_linked_list(nums3)
result3_head = ts.removeElements(list3, val3)
result3 = linked_list_to_list(result3_head)
expected3 = []
print(f"Input: head = {nums3}, val = {val3}, Output: {result3}, Expected: {expected3}, Match: {result3 == expected3}")


