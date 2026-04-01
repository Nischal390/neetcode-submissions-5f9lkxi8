class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = {}
        for i in nums:
            if i in has.keys():
                has[i]+=1
            else:
                has[i]=1

            if has[i]>1:
                return True
        return False               