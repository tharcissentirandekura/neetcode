class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1 #buy = l and sell = r
        max_profit = 0

        while l <= r and r < len(prices):
            print(prices[l],prices[r],l,r)
            profit = prices[r] - prices[l]
            
            if prices[r] < prices[l]:
                l = r #buy price = sell price
            else:
                max_profit = max(profit,max_profit)
            r += 1
        return max_profit




