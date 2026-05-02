class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}
        def dfs(i):
            if i in cache.keys():
                return cache[i]
            if i>= n:
                cache[i]=0
                return cache[i]
            take = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            cache[i]=max(take, skip)
            return cache[i]

        return dfs(0)