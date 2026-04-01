class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for amt in range(1,amount+1):
            for coin in coins:
                if amount>=coin:
                    dp[amt]=min(1+dp[amt-coin],dp[amt])

        return dp[amount] if dp[amount] != amount+1 else -1