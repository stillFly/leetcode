# -*- coding：UTF-8 -*-

# Filename: TwoSum.py
# Description: leetcode 01
# Author: stillFly

str_in = input("输入一个以,分割的数组:")
print(str_in.strip('[]'))
nums = [int(n) for n in str_in.strip('[]').split(",")]
target = int(input("目标值为:"))

for i in range(len(nums)):
    num1 = nums[i]
    for j in range(i+1,len(nums)):
        num2 = nums[j]
        if target == (num1 + num2):
            print("["+str(i)+","+str(j)+"]")
            break
