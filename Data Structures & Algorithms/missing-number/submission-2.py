class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mp = Counter(nums)
        n = len(nums)
        for i in range(n):
            if i in mp:
                continue
            return i

        return n