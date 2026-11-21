class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        slo = head

        while slo:
            slo = slo.next
            l += 1

        limit = l - n

        if limit == 0:
            return head.next

        slow = head

        for _ in range(limit - 1):
            slow = slow.next

        slow.next = slow.next.next

        return head