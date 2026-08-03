import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verify(k):
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/k)
            if hours>h:
                return False
            else:
                return True

        l, r = 1, max(piles) #l = 1, r = 4
        mid = l+(r-l)//2     #
        last_success = max(piles)
        while r>=l:
            if verify(mid):
                last_success = mid
                r = mid-1
            else:
                l = mid+1
            mid = l + (r-l)//2

        return last_success