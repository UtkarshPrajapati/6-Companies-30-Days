class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        else:
            return sum([n//(5**i) for i in range(1,math.floor(math.log(n,5))+1)])