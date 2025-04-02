# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not list1 and not list2: return

        # recursive cases
        if not list1: return ListNode(list2.val, self.mergeTwoLists(None, list2.next))
        if not list2: return ListNode(list1.val, self.mergeTwoLists(list1.next, None))
        if list1.val <= list2.val: return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))