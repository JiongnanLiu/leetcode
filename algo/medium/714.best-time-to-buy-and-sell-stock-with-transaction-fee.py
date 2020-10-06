"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.


"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # you either not buy stock and hold 0 cash at day 0
        # or buy stock stock and hold -price[0] cash at day 0
        # cash = the amount of cash if you didn't buy stock
        # hold = the amount of cash if you buy stock
        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            
            # Cash(i): the cash in hand, if you are not holding the stock at the end of day(i)
            # max(left, right): left = you are not holding stock at the end of day(i-1) and do nothing in day[i]
            #                   right = you hold stock at the end of day[i-1] and sell it at the end of day[i]. cash[i] = hold[i-1] + prices[i] - fee
            # choose the greater one to get the greater potential profit   
            cash = max(cash, hold + prices[i] - fee)
            
            # Hold(i): the cash in hand, if you are holding the stock at the end of day(i)
            # max(left, right): left = you hold the stock at the end of day[i-1] and do nothing in day[i]
            #                   right = you didn't hold the stock at the end of day[i-1] and buy one stock at the end of day[i]. 
            #                           cash_after_buy_stock = cash - prices[i]
            # choose the greater one to get the greater potential profit.
            hold = max(hold, cash - prices[i])
        
        return cash