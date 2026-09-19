# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head

        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        l2 = l1.next
        l1.next = None
        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l2 = prev

        l1 = head
        while l1 and l2:
            next1 = l1.next
            next2 = l2.next

            l1.next = l2
            l2.next = next1

            l1 = next1
            l2 = next2



        

        