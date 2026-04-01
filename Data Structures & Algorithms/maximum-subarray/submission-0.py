class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        subsum = nums[0]

        for n in nums:
            if cursum<0:
                cursum = 0
            cursum += n
            subsum = max(cursum,subsum)

        return subsum