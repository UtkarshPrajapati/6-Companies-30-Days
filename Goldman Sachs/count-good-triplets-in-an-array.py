from sortedcontainers import SortedList as sl
class Solution:
    def goodTriplets(self, A: List[int], B: List[int]) -> int:
        p=[0]*len(A)               
        for i,b in enumerate(B):
            p[b]=i
        pb,prea=sl([p[A[0]]]),[0]      
        for a in A[1:]:       
            pb.add(p[a])
            prea.append(pb.bisect_left(p[a]))
        pb,sufa=sl([p[A[-1]]]),[0]
        for a in reversed(A[:len(A)-1]):
            i=pb.bisect(p[a])
            sufa.append(len(pb)-i)
            pb.add(p[a])
        sufa.reverse()
        ans=0
        for x,y in zip(prea,sufa):
            ans+=x*y
        return ans