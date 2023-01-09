from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sl,ans=SortedList(),0
        mp={x:i for i,x in enumerate(nums1)}
        for i,x in enumerate(nums2):
            x=mp[x]
            left=sl.bisect_left(x)
            ans+=(left*((len(nums2)-x-1)-(len(sl)-left)))
            sl.add(x)
        return ans