# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        answer = dummy
        carry = False
        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val
                l1 = l1.next
            else:
                total = l2.val
                l2 = l2.next

            if carry:
                total += 1
                carry = False

            if total > 9:
                answer.next = ListNode(total % 10)
                carry = True
            else:
                answer.next = ListNode(total)
            
            answer = answer.next
        
        if carry:
            answer.next = ListNode(1)
        
        return dummy.next


        