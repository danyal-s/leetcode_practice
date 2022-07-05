# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            if list1 is not None:
                return list1
            
            if list2 is not None:
                return list2
            
            return None
        
        l1_p = list1
        l2_p = list2
        res_head = list2 if l1_p.val >= l2_p.val else list1
        
        while l1_p and l2_p:
            if l1_p.val >= l2_p.val:

                while l2_p.next is not None and l1_p.val >= l2_p.next.val:
                    l2_p = l2_p.next
                
                l2_p.next, l2_p = l1_p, l2_p.next

            else:
    
                while l1_p.next is not None and l2_p.val >= l1_p.next.val:
                    l1_p = l1_p.next
                
                l1_p.next, l1_p = l2_p, l1_p.next

        
        return res_head
