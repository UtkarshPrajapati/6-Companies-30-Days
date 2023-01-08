class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d,ans={},100001
        for i,n in enumerate(cards):
            if n in d: ans=min(i-d[n]+1,ans)
            d[n]=i
        if ans==100001: return -1
        return ans