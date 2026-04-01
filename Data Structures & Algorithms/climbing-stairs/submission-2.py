class Solution:
    def climbStairs(self, n: int) -> int:
        
        memoi = {1:1, 2:2}

        if n == 1 or n==2:
            return memoi[n]

        if n in memoi.keys():
            return memoi[n]
        
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)