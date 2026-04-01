class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = zip(position,speed)
        fleet = list(fleet)
        fleet.sort()

        stack = []

        for i in range(len(fleet)-1,-1,-1):
            stack.append(fleet[i])
            if len(stack)>=2:
                if (target-stack[-1][0])/stack[-1][1]<=(target-stack[-2][0])/stack[-2][1]:
                    stack.pop()

        return len(stack)