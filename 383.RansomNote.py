'''
Link: https://leetcode.com/problems/ransom-note
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict, mag_dict = Counter(), Counter()
        for char in magazine:
            mag_dict[char] += 1
        
        for char in ransomNote:
            ransom_dict[char] += 1
        
        for key in ransom_dict:
            if key not in mag_dict or mag_dict[key] < ransom_dict[key]:
                return False
        return True