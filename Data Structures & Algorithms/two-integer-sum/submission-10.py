class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i,num in enumerate(nums):
            if target-num in map_:
                return [map_[target-num],i]
            map_[num] = i

        