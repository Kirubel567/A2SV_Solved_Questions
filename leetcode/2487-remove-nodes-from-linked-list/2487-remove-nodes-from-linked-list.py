# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mon_dec =deque()
        curr = head
        while curr: 
            while mon_dec and curr.val>mon_dec[-1].val: 
                mon_dec.pop()
            mon_dec.append(curr)
            curr=curr.next

        head = mon_dec.popleft()
        curr = head
        while mon_dec:
            curr.next=mon_dec.popleft()
            curr=curr.next
        return head 