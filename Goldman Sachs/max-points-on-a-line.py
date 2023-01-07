class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        ans=1
        if n<3: return n
        def slope(p1,p2):
            (x1,y1),(x2,y2)=p1,p2
            if x1==x2: return inf
            return (y2-y1)/(x2-x1)
        for i,p1 in enumerate(points):
            slopes=defaultdict(int)
            for j,p2 in enumerate(points[i+1:]):
                sl=slope(p1,p2)
                slopes[sl]+=1
                ans=max(slopes[sl],ans)
        return ans+1