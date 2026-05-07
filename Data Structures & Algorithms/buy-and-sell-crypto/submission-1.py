class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        n = len(prices)
        buy, sell = 0, 1

        while sell < n:
            profit = prices[sell] - prices[buy]
            if profit > 0:
                total = max(total, profit)
                sell = sell + 1
            else:
                buy = sell
                sell = sell + 1


        return total