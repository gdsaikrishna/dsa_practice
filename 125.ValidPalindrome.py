'''
Link: https://leetcode.com/problems/valid-palindrome
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while end > start and not s[end].isalnum() :
                end -= 1
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
            
            
            
        