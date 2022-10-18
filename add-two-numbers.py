# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # init
        l3 = ListNode(0)
        res = l3
        sum = 0
        # loop to add digits from 2 lists if present and carry forward from sum of previous iteration.
        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # mould unit value from sum into linked list    
            l3.next = ListNode(sum%10)
            l3 = l3.next
            sum //= 10
                
        # return previously stored pointer.
        return res.next

