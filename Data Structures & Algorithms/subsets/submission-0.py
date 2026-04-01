class Solution:
    def backtrack(self, i):
        if i >= self.n:
            self.res.append(self.sub.copy())
            return
        self.sub.append(self.nums[i])
        self.backtrack(i+1)

        self.sub.pop()
        self.backtrack(i+1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.n = len(nums)
        self.sub = []

        self.backtrack(0)

        return self.res