class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # [1,2,3,3,3,4,5]
        #  0 1 2 3 4 5 6
        #  l     m      r
        #if you stop above you cannot find left most and right most index so from this point
        #we continue to do it once left and once right.

        def binarySearch(nums, target, leftBias):  #[5,7,7,8,8,10], 8
            l, r = 0, len(nums)-1      #l=0,r=5
            i = -1                     #i=-1
            while l<=r:
                mid = (l+r)//2         #mid = 2  
                if target>nums[mid]:   #8>7
                    l = mid+1
                elif target<nums[mid]:
                    r = mid-1
                else:
                    i = mid
                    if leftBias:
                        r = mid-1
                    else:
                        l=mid+1
            return i
        
        left_index = binarySearch(nums, target, True)
        right_index = binarySearch(nums, target, False)

        return [left_index, right_index]        