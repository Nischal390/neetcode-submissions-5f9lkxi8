class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num in nums:
            if count[num] > 1:
                return True

        return False