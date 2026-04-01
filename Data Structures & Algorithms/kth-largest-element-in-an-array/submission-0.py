class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return None
        nums = [-num for num in nums]
        
        heapq.heapify(nums)
        
        while k>0:
            ele = heapq.heappop(nums)
            k-=1
            
        return -ele