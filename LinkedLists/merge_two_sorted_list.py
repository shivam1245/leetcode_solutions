from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = flag = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1, temp = list1.next, list1
            else:
                temp.next = list2
                list2, temp = list2.next, list2
        if list1 or list2:
            temp.next = list1 if list1 else list2
        return flag.next
