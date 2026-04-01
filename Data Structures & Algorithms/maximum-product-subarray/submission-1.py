class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1,1

        for num in nums:
            tmp = curMax
            curMax = max(curMax*num, curMin*num,num)
            curMin = min(tmp*num, curMin*num, num)
            res = max(res,curMax)
        
        return res