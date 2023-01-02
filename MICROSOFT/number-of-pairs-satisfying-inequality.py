class Solution:
    def numberOfPairs(self, a: List[int], b: List[int], diff: int) -> int:
        n=len(a)
        s=0
        arr=[]
        c=[i-j for i,j in zip(a, b)]
        for num in c:
            s+=bisect_right(arr,num+diff)
            insort(arr,num)
        return s