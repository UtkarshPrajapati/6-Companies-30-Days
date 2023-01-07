from math import dist
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for x in points:
            d=collections.defaultdict(int)
            for y in points:
                d[dist(x,y)]+=1
            for k in d:
                ans+=d[k]*(d[k]-1)
        return ans