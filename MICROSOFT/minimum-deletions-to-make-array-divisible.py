import math
class Solution:
    def minOperations(self, a: List[int], numsDivide: List[int]) -> int:
        g=math.gcd(*numsDivide)
        for i,b in enumerate(sorted(a)):
            if g%b==0: return i
            if b>g: break
        return -1