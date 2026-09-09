class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell = 0, 1
        profit = 0
        while sell < n:
            get = prices[sell] - prices[buy]
            profit = get if get > profit else profit

            if prices[buy] >= prices[sell]:
                buy = sell
            # else:
            sell += 1
            
        return profit