# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        n1, n2 = l1, l2
        inc, total = 0, 0
        while True:
            if n1 and n2:
                total = n1.val + n2.val + inc
                n1, n2 = l1.next, l2.next
                l1, l2 = n1, n2
            elif n1:
                total = n1.val + inc
                n1 = l1.next
                l1 = n1
            elif n2:
                total = n2.val + inc
                n2 = l2.next
                l2 = n2
            
            cur.val = total % 10
            inc = total // 10

            if not n1 and not n2:
                if inc == 1:
                    cur.next = ListNode(inc)
                break
            
            cur.next = ListNode(0)
            cur = cur.next

        return dummy