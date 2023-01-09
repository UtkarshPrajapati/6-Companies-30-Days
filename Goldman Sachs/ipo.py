class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h,i,p=[],0,sorted(zip(profits,capital),key=lambda l:l[1])
        for _ in range(k):
            while i<len(p) and p[i][1]<=w: heapq.heappush(h,-p[i][0]);i+=1
            if h: w-=heapq.heappop(h)
        return w