class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n=len(nums2)
        m=len(nums1)-n
        del nums1[m:]
        
        print(nums1)
        i,j=0,0

        while i<m and j<n:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>=nums2[j]:
                nums1.insert(i,nums2[j])
                j+=1
                m+=1

        while j<n:
            nums1.insert(i,nums2[j])
            i+=1
            j+=1