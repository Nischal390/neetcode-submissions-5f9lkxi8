class Solution:
    # def maxArea(self, heights: List[int]) -> int:
    #     res = 0

    #     for l in range(len(heights)):
    #         for r in range(l+1, len(heights)):
    #             area = (r - l)*min(heights[l],heights[r])
    #             res = max(res, area)

    #     return res

    #Linear time solution
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        MaxArea = (r-l)*min(heights[l],heights[r])
        while l<r:
            area = (r - l)*min(heights[l],heights[r])
            MaxArea = max(MaxArea, area)

            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            else:
                r-=1

        return MaxArea
                