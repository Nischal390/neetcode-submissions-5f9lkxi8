class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = cur_max = 1

        for num in nums:
            temp = cur_max
            cur_max = max(cur_max*num, num, cur_min*num)
            cur_min = min(temp*num, num, cur_min*num)
            res = max(res,cur_max)
        
        return res