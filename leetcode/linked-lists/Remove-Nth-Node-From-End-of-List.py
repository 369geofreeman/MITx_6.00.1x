# Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?




# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        index = ListNode(0)
        index.next = head
        pointA = pointB = index
        for i in range(n):
            pointA = pointA.next

        while pointA.next != None:
            pointA = pointA.next
            pointB = pointB.next
        else:
            pointB.next = pointB.next.next
        return index.next





# 208 / 208 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14 MB
