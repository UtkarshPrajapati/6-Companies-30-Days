class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def d(p1,p2):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        s=set([d(p1,p2),d(p1,p3),d(p1,p4),d(p2,p3),d(p2,p4),d(p3,p4)])
        return 0 not in s and len(s)==2