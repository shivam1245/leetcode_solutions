"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add these two numbers and return the sum as a linked list.
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
            self, l1: Optional[ListNode],
            l2: Optional[ListNode]
            ) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        carry = 0

        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum >= 10:
                carry = sum // 10
                sum %= 10

            else:
                carry = 0

            p.next = ListNode(sum)
            p = p.next

        if carry:
            p.next = ListNode(carry)

        return dummy.next
