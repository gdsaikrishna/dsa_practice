'''
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 1:
            num, ptr = nums[0], 0
            i = 0
            while i < n:
                if nums[i] != num:
                    nums[ptr+1] = nums[i]
                    num = nums[ptr+1]
                    ptr += 1
                i += 1
            return ptr+1
        return 1
