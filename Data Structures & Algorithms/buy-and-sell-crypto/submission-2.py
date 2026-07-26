class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=r=0
        n = len(prices)
        max_profit=0
        cur_profit=0
        for r in range(n):
            if prices[r]>prices[l]:
                cur_profit = prices[r]-prices[l]
                max_profit = cur_profit if cur_profit>max_profit else max_profit
            else:
                l=r

        return max_profit        