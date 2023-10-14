# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        ptr1 = head
        ptr2 = head
        prev = None
        
        while ptr2 and ptr2.next:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        






          
         