class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]

        curr_max = 0
        l = len(height)
        right_max = [0]*l
        for i in range(1, l):
            if height[i-1]>curr_max:
                curr_max = height[i-1]
            left_max.append(curr_max)

        curr_max = 0
        for i in range(l-2,-1,-1):
            if height[i+1]>curr_max:
                curr_max = height[i+1]
            right_max[i] = curr_max
        

        water = 0
        for i in range(l):
            wall = min(left_max[i], right_max[i])
            if height[i]<wall:
                water += wall-height[i]

        return water