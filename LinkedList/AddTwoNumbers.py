# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new1=ListNode()
        final=new1
        sum1=l1.val+l2.val
        if(sum1>9):
            carry=1
            sum1=sum1%10
            new1.val=sum1
            l1=l1.next
            l2=l2.next
        else:
            carry=0
            new1.val=sum1
            l1=l1.next
            l2=l2.next
        
       

        while l1 is not None and l2 is not None:
            
            sum1=l1.val+l2.val+carry
            if(sum1>9):
                carry=1
                sum1=sum1%10
            else:
                carry=0
            
            newNode=ListNode(sum1)
            newNode.next=None
            new1.next=newNode
            new1=new1.next
            
           
            
            
            
            
            l1=l1.next
            l2=l2.next
        while(l1 is not None):
            l1.val=l1.val+carry
            if(l1.val>9):
                carry=1
                l1.val=l1.val%10
                
            else:
                carry=0
            new1.next=l1
            l1=l1.next
            new1=new1.next
        while(l2 is not None):
            l2.val=l2.val+carry
            if(l2.val>9):
                carry=1
                l2.val=l2.val%10
            else:
                carry=0
            new1.next=l2
            new1=new1.next
            l2=l2.next
        if(carry==1):
            newNode=ListNode(1)
            newNode.next=None
            new1.next=newNode



        return final
        
  
