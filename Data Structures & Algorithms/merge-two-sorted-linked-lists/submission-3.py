# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        goat = peat = ListNode()

        while list1 and list2:
            if list1.val<=list2.val:
                peat.next = list1
                peat = peat.next
                list1 = list1.next
            else:
                peat.next = list2
                list2 = list2.next
                peat = peat.next

        if list1:
            peat.next = list1
        if list2:
            peat.next = list2

        return goat.next