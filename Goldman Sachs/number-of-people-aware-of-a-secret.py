class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp,s,mod=[1]+[0]*forget,0,1000000007
        for i in range(1,n):
            dp[i%forget]=s=(s+dp[(i-delay)%forget]-dp[i%forget])%mod
        return sum(dp)%mod