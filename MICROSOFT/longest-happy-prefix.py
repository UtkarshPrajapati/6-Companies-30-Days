class Solution:
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        j,i,dp=0,1,[0]*n
        while i<n:
            if s[i]==s[j]:
                j+=1
                dp[i]=j
            elif j>0:
                i-=1
                j=dp[j-1]
            i+=1
        return s[0:j]