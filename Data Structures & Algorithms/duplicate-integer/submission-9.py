class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
            if hash_map[num]>1:
                return True

        return False

        