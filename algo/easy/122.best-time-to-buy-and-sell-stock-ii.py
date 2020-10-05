class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #find the valley (where valley's price is less than the price both prior to it and next to it)
        #find the peak (where peak's price is greater than the price both prior to it and next to it)
        # peak2 - vally2 + peak1 - valley1 is always greater than peak2 - valley1
        #             
        #            6               
        #       5   / 
        #      / \ /   
        #     /   3     
        #    /          
        #   1                   
        #
        #  (5-1) + (6-3) is always greater than (6-1)
        # so we need to find the 5 (peak) and 3 (valley)
        #
        profit = 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        while(i < len(prices)-1):
            while(i < len(prices)-1 and prices[i] >= prices[i+1]):
                i += 1
            #when prices[i+1] is greater than prices[i], we find the valley at i
            valley = prices[i] 
            while(i < len(prices) - 1 and prices[i] <= prices[i+1]):
                i += 1
            #when prices[i+1] is less than prices[i], we find the peak at i
            peak = prices[i]
            profit += peak - valley
        return profit