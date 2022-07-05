# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        #O(n^2) time, O(1) space
        cur_node = head
        cur_node_delayed = head
        
        if cur_node.next is None:
            return False
        
        if cur_node.next.next is None:
            return False
        

        while cur_node.next is not None and cur_node.next.next is not None:
            cur_node = cur_node.next.next
            cur_node_delayed = cur_node_delayed.next
            
            if cur_node == cur_node_delayed:
                return True
        
        return False


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time, O(n) space
        n_addresses = set()
        
        cur_node = head
        while cur_node.next is not None:
            if id(cur_node) in n_addresses:
                return True
            n_addresses.add(id(cur_node))
            cur_node = cur_node.next
        
        return False
