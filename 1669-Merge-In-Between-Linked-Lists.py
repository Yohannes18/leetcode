# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        preA = list1
        for _ in range(a - 1):
            preA = preA.next
        
        postB = preA
         
        for _ in range(b - a + 2):
            postB = postB.next
        
        endList2 = list2

        while endList2.next:
            endList2 = endList2.next
        endList2.next = postB

        preA.next = list2
        return list1
        