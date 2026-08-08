class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i,num in enumerate(nums):
            if target-num in index_map.keys():
                return [index_map[target-num],i]
            index_map[num] = i