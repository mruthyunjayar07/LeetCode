from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k nodes left, stop

            group_next = kth.next

            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev.next      # tail of the reversed group
            group_prev.next = kth      # kth is now the new head
            group_prev = tmp           # advance group_prev to the tail

        return dummy.next