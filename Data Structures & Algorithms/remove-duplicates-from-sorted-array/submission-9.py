class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.append('inf')
        dup = []
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
                
            dup.append(nums[i])
        
        nums[:len(dup)]=dup
        return len(dup)