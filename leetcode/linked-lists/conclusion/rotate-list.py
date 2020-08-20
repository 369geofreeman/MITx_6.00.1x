# Rotate List

# Given a linked list, rotate the list to the right by k places, where k is non-negative.
# 
# Example 1:
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #1. if there is no node or only one node in the list
        #just return head
        if not head or not head.next:
            return head

        #2. we do not need to move k times but move k % len(lst) if k% len(lst) != 0
        # so we need walk through the list to find the length
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        # update k, which is the actual time we need to move right
        k = k % n
        if k == 0:
            return head


        # initialize two pointer,
        # one is point the head
        # one is point the position we need to rotate

        p1, p2 = head, head

        # walk p2 to the position of rotate
        for _ in range(k):
            p2 = p2.next


        # now we walk p1 and p2 till p2 or p2.next is None
        # then p1 would be the rotation position
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next

        res = p1.next

        # link the two part and update the tail
        p1.next = None
        p2.next = head

        return res



# 231 / 231 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 14.1 MB
