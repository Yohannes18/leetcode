# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num, second_num = 0, 0
        multiplier = 1
        
        while l1:
            first_num += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next
            
        multiplier = 1
        
        
        while l2:
            second_num += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next
        
        total_sum = first_num + second_num
        
        
        if total_sum == 0:
            return ListNode(0)
      
        dummy = ListNode(0)
        current = dummy
        
        while total_sum > 0:
            current.next = ListNode(total_sum % 10)
            current = current.next
            total_sum //= 10
        
        return dummy.next