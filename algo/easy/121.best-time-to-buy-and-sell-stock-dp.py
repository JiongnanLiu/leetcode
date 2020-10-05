class Solution:
    def maxProfit(self, prices):
        if not prices: 
            return 0
        sell_prc = max(prices)
        max_prf = 0
        for p in prices:
            if p < sell_prc:
                sell_prc = p
            max_prf = max(p - sell_prc, max_prf)
            
        return max_prf