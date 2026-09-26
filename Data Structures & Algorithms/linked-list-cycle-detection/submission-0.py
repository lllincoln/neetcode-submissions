# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        current_node = head
        visited = set()

        while current_node != None:
            current_node_hash = hash(current_node)
            
            if current_node_hash in visited:
                return True
            
            visited.add(current_node_hash)
            current_node = current_node.next
        
        return False