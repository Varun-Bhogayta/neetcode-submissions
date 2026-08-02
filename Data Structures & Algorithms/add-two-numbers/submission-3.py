# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        c1 = l1
        c2 = l2
        c3 = sum_head
        carry = 0
        while c1 and c2:
            curr_sum = c1.val + c2.val + carry
            if curr_sum > 9:
                carry = 1
                curr_sum -= 10
            else:
                carry = 0
            c3.next = ListNode(curr_sum)

            c1 = c1.next
            c2 = c2.next
            c3 = c3.next

        while c1:
            if carry:
                curr_sum = c1.val + carry
                if curr_sum > 9:
                    carry = 1
                    curr_sum -= 10
                else:
                    carry = 0
                c3.next = ListNode(curr_sum)
                c1 = c1.next
                c3 = c3.next
            else:
                c3.next = c1
                break

        while c2:
            if carry:
                curr_sum = c2.val + carry
                if curr_sum > 9:
                    carry = 1
                    curr_sum -= 10
                else:
                    carry = 0
                c3.next = ListNode(curr_sum)
                c2 = c2.next
                c3 = c3.next
            else:
                c3.next = c2
                break

        if carry:
            c3.next = ListNode(carry)

        sum_head = sum_head.next        

        return sum_head        