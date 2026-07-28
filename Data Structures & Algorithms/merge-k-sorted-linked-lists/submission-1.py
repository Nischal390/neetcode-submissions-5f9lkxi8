# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):

            l3 = ListNode()
            dummy = l3

            while l1 and l2:
                if l1.val<l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                l3 = l3.next
            
            if l1:
                l3.next = l1 
            else:
                l3.next = l2

            return dummy.next

        dummy_list = None
        for i,list_ in enumerate(lists):
            dummy_list = merge(dummy_list,list_)


        return dummy_list