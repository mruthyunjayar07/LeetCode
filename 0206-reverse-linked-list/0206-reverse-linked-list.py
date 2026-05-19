class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next
            curr.next = prev        # reverse the pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev                 # prev is new head