# Linked List Cycle


# Given a linked list, determine if it has a cycle in it.
# 
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# 
# 
# 
# Example 1:
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# 
# 
# Example 2:
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# 
# 
# Example 3:
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


 #Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowPointer = head
        fastPointer = head
        while slowPointer and fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        return False



# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 17 MB
