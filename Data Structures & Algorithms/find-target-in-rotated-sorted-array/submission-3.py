class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = (l+r)//2

        while l<=r:
            #left is sorted
            if nums[mid] == target:
                return mid
            elif nums[l]<=nums[mid]:
                if target <= nums[mid] and target>=nums[l]:
                    r = mid-1
                    mid = (r+l)//2
                else:
                    l = mid + 1
                    mid = (l+r)//2
            #right is sorted
            else:
                if target >= nums[mid] and target<=nums[r]:
                    l = mid +1
                    mid = (l+r)//2
                else:
                    r = mid-1
                    mid = (l+r)//2

        return -1