# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = end = 0
        if len(s)==0:
            return 0

        while start<len(s) and end<len(s):
            if start>=end:
                end += 1

            middle_str = s[start:end+1]
            if len(middle_str)== len(set(middle_str)):
                max_len = max(max_len,len(middle_str))
                end += 1
            else:
                start += 1
        return max_len


class Solution2:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        # "aab"
        for i in range(len(s)):
            print("strat of the loop")
            print(s[i])
            print(usedChar)
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            print("end of the loop")
            print(usedChar)
            print(maxLength)
            usedChar[s[i]] = i
        return maxLength

Solution2().lengthOfLongestSubstring("ababab")