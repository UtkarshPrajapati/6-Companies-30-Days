class Solution(object):
    def findUnsortedSubarray(self, nums):
        n=len(nums)
        if n<2: return 0
        end,prev = 0,nums[0]
        for i in range(n):
            if nums[i]<prev: end=i
            else: prev=nums[i]
        start,prev=n-1,nums[n-1]
        for i in range(n-1,-1,-1):
            if prev< nums[i]: start=i
            else: prev=nums[i]
        if end!=0: return end-start+1
        else: return 0