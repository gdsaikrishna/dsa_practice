'''
Link: https://leetcode.com/problems/rotate-array
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        n = len(nums)
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range(k, (n+k)//2):
            nums[i], nums[n-1-i+k] = nums[n-1-i+k], nums[i]