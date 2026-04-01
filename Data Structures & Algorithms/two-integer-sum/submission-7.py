class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in visited:
                return [visited[target-nums[i]],i]
            visited[nums[i]] = i

        return [-1,-1]