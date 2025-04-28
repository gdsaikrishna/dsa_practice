'''
Link: https://leetcode.com/problems/h-index
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_ci = max(citations)
        arr = [0 for i in range(max_ci+1)]
        for ci in citations:
            arr[ci] += 1
        res, acc = 0, 0
        for i in range(max_ci, -1, -1):
            acc += arr[i]
            if acc >= i:
                return i
        return 0