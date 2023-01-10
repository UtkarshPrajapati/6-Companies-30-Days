class Solution:
    def maximumGood(self, A: List[List[int]]) -> int:
        n,ans=len(A),0
        def check(perm):
            for i in range(n):
                if perm[i]=='0': continue
                for j in range(n):
                    if A[i][j]==2: continue
                    if (A[i][j]==1 and perm[j]=='0') or (A[i][j]==0 and perm[j]=='1'): 
                        return False
            return True
        for num in range(1<<n,1<<(n + 1)):
            p=bin(num)[3:]
            if check(p): 
                ans=max(ans,p.count('1'))
        return ans