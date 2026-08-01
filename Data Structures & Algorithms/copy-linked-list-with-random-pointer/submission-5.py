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
        if not head:
            return None
        mp = {}
        curr = head
        head2 = Node(x=0)
        curr2 = head2
        while curr:
            curr2.next = Node(curr.val,None,curr.random)
            curr2 = curr2.next
            mp[curr] = curr2
            curr = curr.next
        head2 = head2.next
        curr2 = head2
        while curr2:
            if curr2.random is not None:
                curr2.random = mp[curr2.random]
            curr2 = curr2.next
        return head2

