class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = sorted(list(set(nums)))
        l = len(dup)
        nums[:l]=dup
        return l