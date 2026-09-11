class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        l = less
        g = greater
        curr = head
        while curr:
            if curr.val < x:
                l.next = curr
                l = l.next
            else:
                g.next = curr
                g = g.next
            curr = curr.next
        g.next = None
        l.next = greater.next
        return less.next