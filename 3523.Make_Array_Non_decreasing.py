'''
Link: https://leetcode.com/problems/make-array-non-decreasing/description/

You are given an integer array nums. In one operation, you can select a subarray and replace it with a single element equal to its maximum value.

Return the maximum possible size of the array after performing zero or more operations such that the resulting array is non-decreasing.

 

Example 1:

Input: nums = [4,2,5,3,5]

Output: 3

Explanation:

One way to achieve the maximum size is:

Replace subarray nums[1..2] = [2, 5] with 5 → [4, 5, 3, 5].
Replace subarray nums[2..3] = [3, 5] with 5 → [4, 5, 5].
The final array [4, 5, 5] is non-decreasing with size 3.

'''

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        res = prev = 0
        for num in nums:
            if prev <= num:
                prev = num
                res += 1
        return res