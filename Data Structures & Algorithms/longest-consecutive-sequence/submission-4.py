class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if max(nums)>-min(nums):
            hash = [0]*(2*max(nums)+1)
        else:
            hash = [0]*(2*-min(nums)+1)
        
        if min(nums)<0:
            for i in nums:
                hash[i-min(nums)]+=1
        else:
            for i in nums:
                hash[i]+=1

        rod = []
        count = 0
        for i in range(len(hash)):
            if hash[i]>0:
                count+=1
            if hash[i]==0:
                rod.append(count)
                count=0
        rod.append(count)

        if not rod:
            return 1
        else:
            return max(rod)