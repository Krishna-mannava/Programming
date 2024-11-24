# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        final = res
        while(head):
            if(head.val == val):
                res.next = head.next
            else:
                res = res.next
            head = head.next
        return final.next