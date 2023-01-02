class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s=sum(nums)
        n=len(nums)
        r=curr=sum(i*j for i,j in enumerate(nums))
        while nums:
            curr+=s-nums.pop()*n
            r=max(curr,r)
        return r