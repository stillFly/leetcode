# Definition for single-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        l1 type: ListNode
        l2 type: ListNode
        rtype: ListNode
        """
        result_str = ''
        carry_bit = 0
        while l1.next != None:
            value = l1.val + l2.val + carry_bit
            if value >= 10:
                value = value - 10
                carry_bit = 1
            l = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            if not l.next:
                result_str = result_str + str(l.val) + ' -> '
            else:
                result_str = result_str + str(l.val)
        print(result_str)

        return res_list
