###############################################################################
'''

Given a sorted linked list, delete all duplicates such that each element appear only once.
Example:
Input: 1->1->2
Output: 1->2

Example:
Input: 1->1->2->3->3
Output: 1->2->3
'''
################################################################################

'''
Brute force (while loop) solution:
Time complexities:  O(n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head == None:
            return head

        current = head.next
        prev = head

        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next

        return head
