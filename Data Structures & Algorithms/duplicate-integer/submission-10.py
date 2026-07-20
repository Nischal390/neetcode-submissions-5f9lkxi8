class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            hash_map[str(num)] = hash_map.get(str(num), 0)+1
            if hash_map[str(num)] == 2:
                return True
        return False

        

        