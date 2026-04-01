class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""

        mp = Counter(s)

        arr = []

        for key in mp:
            heapq.heappush(arr,(-1*mp[key], key))

        prev = None

        while arr:
            (freq, char) = heapq.heappop(arr)
            freq = -1*freq
            if prev:
                heapq.heappush(arr,prev)
                prev = None

            res+=char
            if freq>1:
                prev = (-1*(freq-1),char)

        if prev:
            return ""

        return res