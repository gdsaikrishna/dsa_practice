'''
Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
'''

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_count = len(set(nums))
        count = Counter()
        left = 0
        res = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) == total_count:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += left
        return res
