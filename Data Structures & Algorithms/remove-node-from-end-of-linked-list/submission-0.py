# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = -n
        f = s = head
        while f :
            print(i,f.val)
            i+=1
            f = f.next
            if i>1:
                s = s.next
        
        if i<=0:
            return head.next

        if s.next:
            s.next = s.next.next
        return head  