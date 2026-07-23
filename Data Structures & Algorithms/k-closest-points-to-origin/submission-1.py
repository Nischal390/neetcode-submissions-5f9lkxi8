class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            val = (x**2 + y**2)**0.5
            points[i].append(val)

        points.sort(key = lambda p:p[2])

        return [p[:2] for p in points[:k]]