# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1he = ListNode(0)
        l1 = l1he

        while list1 and list2:
            if list1.val<=list2.val:
                l1.next = list1
                l1 = l1.next
                list1 = list1.next
            else:
                l1.next = list2
                l1 = l1.next
                list2 = list2.next
        if list1:
            l1.next = list1
            l1 = l1.next
            list1 = list1.next
        if list2:
            l1.next  = list2
            l1 = l1.next
            list2 = list2.next

        return l1he.next

            