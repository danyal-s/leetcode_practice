# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        self.new_head = None
        self._reverseList(head)
        return self.new_head
        
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is not None:
            next_node = self._reverseList(head.next)
            next_node.next = head
            head.next = None
        else:
            self.new_head = head

        return head
