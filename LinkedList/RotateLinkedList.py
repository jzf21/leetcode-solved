# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#61
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        new1=head
        count=0
        while(new1.next is not None):
            count+=1
            new1=new1.next
        new1.next=head
        temp1=new1
        
        
        for i in range((count-k+1)%(count+1)):
            new1=new1.next
        temp1=new1.next
        new1.next=None

        return temp1
            
