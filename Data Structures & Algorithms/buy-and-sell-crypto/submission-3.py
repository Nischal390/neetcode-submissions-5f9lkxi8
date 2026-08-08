class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l,r = 0,0
        n = len(prices)
        for r in range(n):
            if prices[r]<prices[l]:
                l = r
            else:
                max_profit = max(prices[r]-prices[l], max_profit)

        return max_profit