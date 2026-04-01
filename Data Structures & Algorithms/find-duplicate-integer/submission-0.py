class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        has = {}

        for i in nums:
            if i in has:
                return i
            else:
                has[i]=1

        return False