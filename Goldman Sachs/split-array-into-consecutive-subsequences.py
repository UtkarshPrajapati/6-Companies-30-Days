class Solution:
	def isPossible(self, nums: List[int]) -> bool:
		if len(nums)<3: return False
		d=collections.Counter(nums)
		sub=collections.defaultdict(int)
		for i in nums:
			if d[i]==0:
				continue
			d[i]-=1
			if sub[i-1]>0:
				sub[i-1]-=1
				sub[i]+=1
			elif d[i+1] and d[i+2]:
				d[i+1]-=1
				d[i+2]-=1
				sub[i+2]+=1
			else:
				return False
		return True