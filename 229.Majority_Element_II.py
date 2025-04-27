'''
Link: https://leetcode.com/problems/majority-element-ii/

Concept: Boyer-Moore Voting Algorithm

Description: Given an integer array of size n, find all elements that appear more than n/3 times.
Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        count1, count2, c1,c2 = 0, 0, 0, 1
        for num in nums:
            if c1 == num:
                count1 += 1
            elif c2 == num:
                count2 += 1
            elif count1 == 0:
                count1, c1 = 1, num
            elif count2 == 0:
                count2, c2 = 1, num
            else:
                count1, count2 = count1-1, count2-1
        
        return [n for n in (c1,c2) if nums.count(n) > len(nums)/3]