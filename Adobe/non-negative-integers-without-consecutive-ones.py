class Solution:
    def findIntegers(self, n: int) -> int:
        ans,l,f=0,0,[1,2]
        for i in range(2,30):
            f.append(f[-1]+f[-2])
        for i in range(30,-1,-1):
            if (1<<i)&n:
                ans+=f[i]
                if l:ans-=1;break
                l=1
            else:l=0
        return ans+1