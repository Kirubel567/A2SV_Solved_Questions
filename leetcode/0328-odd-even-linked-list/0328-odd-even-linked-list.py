# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: 
            return head 

        counter = 0
        curr = head 
        connect = head.next #start of even(start of connection)

        while curr:
            curr = curr.next 
            counter += 1
            
        curr = head 
        while curr.next.next: 
            temp = curr.next
            curr.next = curr.next.next 
            curr = temp

        if counter%2 == 0:
            curr.next.next = None 
            curr.next = connect 
        else: 
            curr.next.next = connect 
            curr.next = None 
        
        return head 
        


            



