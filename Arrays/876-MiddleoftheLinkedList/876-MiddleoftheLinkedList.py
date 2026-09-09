# Last updated: 9/9/2026, 10:36:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        slow = head
9        fast = head
10        while fast and fast.next and slow :
11            slow = slow.next
12            fast = fast.next.next
13        return slow
14    
15        