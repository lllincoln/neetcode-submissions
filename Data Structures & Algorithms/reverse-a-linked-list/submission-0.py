# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1-->2-->3
        # 1<--2<--3

        # current_node = 3
        # current_node.next = None
        # next_node = 3
        # previous_node = 2

        current_node = head
        previous_node = None

        while True:
            if not current_node:
                break
            
            next_node = current_node.next
            
            # Perform the reverse swap
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        return previous_node