class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()
        def dfs(node):
            for j in adj[node]:
                if j not in visit:
                    visit.add(j)
                    dfs(j)


        res = 0
        for j in range(n):
            if j not in visit:
                dfs(j)
                res+=1

        return res