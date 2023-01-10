class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        s,d=0,{}
        for i,a in enumerate(nums):
            k=a-int(str(a)[::-1])
            if k in d.keys(): d[k]+=[i]
            else: d[k]=[i]
        for i in d.keys():
            m=len(d[i])
            s+=(m*(m-1)//2)%(1000000007)
        return s%(1000000007)