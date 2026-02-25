class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)

        # create slow & fast, then point to dummy_head
        slow = fast = dummy_head

        # 'fast' faster than 'slow' n+1
        # there is n between 'fast' and 'slow'
        for i in range(n+1):
            fast = fast.next
        
        # slow & fast work together
        # when fast.next = null, than slow is just on Nth-1 from end
        while fast:
            fast = fast.next
            slow = slow.next

        # remove Nth node:
        slow.next = slow.next.next

