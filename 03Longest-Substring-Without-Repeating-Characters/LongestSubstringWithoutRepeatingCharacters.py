# -*- coding：UTF-8 -*-

# Filename: LongestSubstringWithoutRepeatingCharacters.py
# Description: leetcode 03
# Author: stillFly

class Solution:
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        sub_s = ''
        cur_length = len(sub_s)
        max_length = cur_length
        for letter in s:
            if letter not in sub_s:
                sub_s = sub_s + letter
            else:
                cur_length = len(sub_s)
                if cur_length > max_length:
                    max_length = cur_length
                index = sub_s.find(letter) + 1
                sub_s = sub_s[index:] + letter
        cur_length = len(sub_s)
        if cur_length > max_length:
            max_length = cur_length

        print(sub_s)
        print(max_length)
        return max_length

Solution.lengthOfLongestSubstring('dvdf')
