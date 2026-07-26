from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counts = Counter(nums)
        n = len(nums)//3
        for num,count in counts.items():
            if count >n:
                res.append(num)

        return res
