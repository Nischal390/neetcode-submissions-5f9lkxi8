class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        past = []
        future = []
        solution = []

        for i in range(len(nums)):
            if i == 0:
                past.append(1)
            else:
                past.append(past[i-1]*nums[i-1])
        for i in range(len(nums)):
            if i == 0:
                future.append(1)
            else:
                future.append(future[i-1]*nums[len(nums)-i])
        future.reverse()

        for i in range(len(nums)):
            solution.append(past[i]*future[i])

        return solution