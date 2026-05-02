from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache
        def dfs(i):
            if i>= n:
                return 0
            take = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            return max(take, skip)

        return dfs(0)