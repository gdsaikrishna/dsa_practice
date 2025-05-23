'''
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: 
            return 0
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) 
        return sum(profit)
