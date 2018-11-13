# -*- coding：UTF-8 -*-

# Filename: AddTwoNumbers.py
# Description: leetcode 02
# Author: stillFly

# class ListNode:
#     def __init__(self, x):
#        self.val = x
#        self.next = None
class Solution:
    def listToNum(l):
        num = 0
        cnt = 0
        while l.next != None:
            num = num + l.val*(10**cnt)
            cnt = cnt + 1
            l = l.next
        num = num + l.val*(10**cnt)
        return num

    def numToList(num):
        num_list = []
        num_list.append(num % 10)
        num = num // 10
        while num != 0:
            num_list.append(num % 10)
            num = num // 10
        list_node = [ListNode(n) for n in num_list]
        for i in range(len(list_node)):
            if list_node[i] == list_node[-1]:
                break
            else:
                list_node[i].next = list_none_in[i]
        return list_node

    def addTwoNumbers(self, l1, l2):
        """
        l1 type: ListNode
        l2 type: ListNode
        rtype: ListNode
        """
        num1 = listToNum(l1)
        num2 = listToNum(l2)
        res_list = numToList(num1 + num2)

        return res_list[0]
