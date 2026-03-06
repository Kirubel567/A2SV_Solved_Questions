# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #have three pointers 1-> to track the pref 2-> track the curr 3 -> tracking the future(the next pointer to reverse)
        #start from a dummy node, behind at the dummy, middle at the current and curr at curr.next
        behind = None 
        curr = head 
 

        while curr and curr.next: 
            lead = curr.next #keep the connection 
            curr.next = behind #severe the connection and reverse

            behind = curr #now current becomes behind 
            curr = lead #make the curr to the lead
        if curr: 
            curr.next = behind
        
        return curr
