# Linked List Cycle II

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# 
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# 
# Note: Do not modify the linked list.
# 
#  
# 
# Example 1:
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# 
# 
# Example 2:
# 
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# 
# 
# Example 3:
# 
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
# 
# 
#  
# 
# Follow-up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        f_cycle = s_cycle = head
        while f_cycle and f_cycle.next:
            f_cycle = f_cycle.next.next
            s_cycle = s_cycle.next
            if f_cycle == s_cycle:
                index = head
                while index != s_cycle:
                    s_cycle = s_cycle.next
                    index = index.next
                return s_cycle


# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 16.7 MB
