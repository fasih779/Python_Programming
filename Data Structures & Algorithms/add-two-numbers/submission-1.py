
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        dummy = node = ListNode()
        carry = 0

        while n1 or n2 or carry:
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0

            value = v1 + v2 + carry

            carry = value // 10
            digit = value % 10

            node.next = ListNode(digit)

            node = node.next

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        return dummy.next