class Solution:
    def knightProbability(self, n: int, k: int, row0: int, col0: int) -> float:
        adj_list=defaultdict(list)
        for row in range(n):
            for col in range(n):
                for dx,dy in ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)):
                    pos=(row+dx,col+dy)
                    if 0<=pos[0]<n and 0<=pos[1]<n:adj_list[(row,col)].append(pos)
        @cache
        def f(pos,h):
            if h==k:return 1
            res=0
            for next_pos in adj_list[pos]: res+=f(next_pos,h+1)
            return res            
        return f((row0,col0),0)/8**k