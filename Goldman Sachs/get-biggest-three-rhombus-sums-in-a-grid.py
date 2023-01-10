class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        l,n,m=[],len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                ans,d=grid[i][j],1
                l.append(ans)
                while(i+d<n and j>=d and j+d<m):
                    a,b,c,dum=i+d,j+d,j-d,0
                    ans+=grid[a][b]+grid[a][c]
                    while(True):
                        c+=1;b-=1;a+=1
                        if(c==m or b==0 or a==n): break
                        if(c==b): dum+=grid[a][b];l.append(ans+dum);break
                        dum+=grid[a][b]+grid[a][c]
                    d+=1
        return sorted(list(set(l)),reverse=True)[:3]