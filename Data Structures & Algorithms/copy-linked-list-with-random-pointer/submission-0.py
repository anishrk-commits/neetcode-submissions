"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        new = dummy
        curr = head
        random = {}
        i = 0
        
        while curr:
            new.next = Node(curr.val)
            new = new.next
            random[curr] = new
            curr = curr.next
        
        new = dummy.next
        curr = head

        while curr:

            new.random = random.get(curr.random, None)
            curr = curr.next
            new = new.next

        return dummy.next
        
