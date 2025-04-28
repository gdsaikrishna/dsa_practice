'''
Link: https://leetcode.com/problems/jump-game
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPositionReached = 0
        lastPos = len(nums) -1
        for index,num in enumerate(nums):
            maxPositionReached = max(index + num, maxPositionReached)
            if maxPositionReached == index and num == 0 and index != lastPos:
                return False
        return True if maxPositionReached >= lastPos else False