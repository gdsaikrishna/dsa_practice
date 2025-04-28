'''
Link: https://leetcode.com/problems/isomorphic-strings
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic, dic1 = {}, {}
        for i,char in enumerate(s):
            if char in dic and dic[char] != t[i]:
                return False
            if t[i] in dic1 and dic1[t[i]] != char:
                return False
            dic[char] = t[i]
            dic1[t[i]] = char
        return True
