class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        # Gives next greater node
        nxt_greater = self.removeNodes(node.next)

        node.next = nxt_greater
        if not nxt_greater or node.val >= nxt_greater.val:
            return node
        return nxt_greater