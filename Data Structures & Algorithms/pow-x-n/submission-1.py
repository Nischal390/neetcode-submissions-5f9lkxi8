class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x,n):
            n = abs(n)
            if n == 0:
                return 1
            elif n%2 ==0:
                a = helper(x,n//2)
                return a*a
            elif n%2 != 0:
                a = x*helper(x,n-1)
                return a
        
        if x == 0:
            return 0
        else:
            return helper(x,n) if n>0 else 1/helper(x,n)