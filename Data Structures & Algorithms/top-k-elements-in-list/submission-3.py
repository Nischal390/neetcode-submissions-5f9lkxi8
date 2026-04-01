class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hush = [0]*2001
        out = []
        for num in nums:
            hush[num+1000] = hush[num+1000]+1

        rod = sorted(hush)[-k:]
        for i in rod:
            out.append(hush.index(i)-1000)
            hush[hush.index(i)]=0


        return out