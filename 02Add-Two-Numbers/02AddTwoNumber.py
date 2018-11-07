class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def listToNum(l):
        num = 0
        cnt = 0
        while l.next != None:
            num = num + l.val*(10**cnt)
            cnt = cnt + 1
            l = l.next
        return num

    def numToList(num):
        pass

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        l1 type: ListNode
        l2 type: ListNode
        rtype: ListNode
        """
        num1 = listToNum(l1)
        num2 = listToNum(l2)
        res_list = numToList(num1 + num2)

        return res_list
