# Palindrome Linked List


# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# Input: 1->2
# Output: false
# Example 2:
# 
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        fast = head # since fast pointer is twice as fast as slow pointer, by the time fast pointer                           reached None, slow pointer will be at middle of the linked list

        slow = self.reverse(slow)   # reversed the second half of the linked list

        while slow != None: # by the time slow pointer reached None, we know that it is a palindrome
                            # linked List. If not, if will be checked by "fast.val != slow.val"
            if fast.val != slow.val:
                return False

            slow = slow.next
            fast = fast.next

        return True



    def reverse(self, slow):    # revisit reversed linked list question

        prev = None
        next = None

        while slow != None:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        return prev


# 26 / 26 test cases passed.
# Status: Accepted
# Runtime: 116 ms
# Memory Usage: 24.1 MB
