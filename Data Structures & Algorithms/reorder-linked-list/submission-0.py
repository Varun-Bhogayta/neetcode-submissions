# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        curr = head
        n = len(arr)
        for i in range(n-1,n//2-1,-1):
            next_n = curr.next
            curr.next = arr[i]
            arr[i].next = next_n
            curr = next_n
            print(arr[i].val)
        arr[n//2].next = None


            