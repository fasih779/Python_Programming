# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0,1,2,3,4,5,6]
        #  h           l
        # [0,1,2,3][4,5,6]
        # [0,1,2,3][6,5,4]
        #  h        l
        #    h        l
        #      h        l
        #        h        l

        # find the middle
        slow = fast = ListNode(0, head)
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        assert slow is not None
        rightHalf = slow.next
        slow.next = None

        # reverse the right half
        prev, cur = None, rightHalf
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        # merge two lists
        cur1, cur2 = head, prev
        while cur1 and cur2:
            nxt1, nxt2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nxt1
            cur1, cur2 = nxt1, nxt2
            