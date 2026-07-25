# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        l3 = dummy

        while l1 or l2 or carry:
            if l1 and l2:
                value = l1.val+l2.val+carry
                carry = value//10
                value = value%10
                l3.next = ListNode(value)
                l1 = l1.next
                l2 = l2.next
                l3 = l3.next
                continue
            if l1 or l2:
                if l1:
                    value = l1.val+carry
                    l1 = l1.next
                if l2:
                    value = l2.val+carry
                    l2=l2.next
                carry = value//10
                value = value%10
                l3.next = ListNode(value)
                l3=l3.next
                continue
            if not l1 and not l2 and carry:
                l3.next  = ListNode(carry)
                carry = 0

        return dummy.next