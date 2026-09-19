# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        count = head
        while count:
            count = count.next
            length += 1
        
        pos = length - n

        curr, prev = head, None

        for i in range(pos):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            head = curr.next

        return head
