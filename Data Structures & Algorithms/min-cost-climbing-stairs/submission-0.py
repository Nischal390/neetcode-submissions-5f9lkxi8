class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [100*n]

        def walking(k,amount):
            
            if k<=1:
                amount+=cost[k]
                res[0] = min(res[0],amount)
                print
                return

            amount+=cost[k]
            walking(k-1,amount)

            walking(k-2,amount)

        walking(n-1,0)
        walking(n-2,0)

        return res[0]