class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) <= 0:
            return profit
        cost = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < cost:
                cost = prices[i]
            if prices[i] - cost > profit:
                profit = prices[i] - cost
        return profit