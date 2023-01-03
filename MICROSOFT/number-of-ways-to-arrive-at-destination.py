class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g=defaultdict(list)
        for u,v,t in roads:
            g[u].append([v,t])
            g[v].append([u,t])
        dist,ways=[math.inf]*n,[0]*n
        dist[0],ways[0],minHeap=0,1,[(0, 0)]
        while minHeap:
            d,u=heappop(minHeap)
            if dist[u]<d:
                continue
            for v,time in g[u]:
                if dist[v]>d+time:
                    dist[v]=d+time
                    ways[v]=ways[u]
                    heappush(minHeap,(dist[v],v))
                elif dist[v]==d+time:
                    ways[v]=(ways[v]+ways[u])%1000000007
        return ways[-1]