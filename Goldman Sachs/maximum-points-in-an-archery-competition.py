class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.ans,self.best=0,None
        def dp(k,rem,score,bobArrows): 
            if k==12: 
                if score>self.ans: 
                    self.ans=score 
                    self.best=bobArrows[::]
                return
            dp(k+1,rem,score,bobArrows)
            need=aliceArrows[k]+1
            if rem>=need: 
               old=bobArrows[k]
               bobArrows[k]=need
               dp(k+1,rem-need,score+k,bobArrows)
               bobArrows[k]=old
        dp(0,numArrows,0,[0]*12)
        self.best[0]+=numArrows-sum(self.best)
        return self.best