class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n

        def find(k):
            res = par[k]

            while par[res] != res:
                par[k] = par[par[k]]
                res = par[k]
            return res



        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0

            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
                

            else:
                par[p1] = p2
                rank[p2]+=rank[p1]
            return 1
        
        ans = n
        for k1,k2 in edges:
            ans -= union(k1,k2)

        return ans