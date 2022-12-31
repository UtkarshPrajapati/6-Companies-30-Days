class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans=[]
        self.func([],1,k,n)
        return self.ans
    def func(self,a,s,k,n):
        if k==0 and n==0:
            self.ans.append(a)
            return 
        if k==0 or n<=0 or n>45:
            return
        for i in range(s,10):
            self.func(a+[i],i+1,k-1,n-i)