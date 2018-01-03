# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_r = ListNode(0)
        l_r2 = l_r
        offset = 0
        while l1 or l2 or offset:
            tempv = (l1.val if l1 else 0)+(l2.val if l2 else 0)+offset
            l_r2.next = ListNode(tempv%10)
            if tempv >= 10 :
                offset = 1
            else:
                offset = 0
            l_r2 = l_r2.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return l_r.next