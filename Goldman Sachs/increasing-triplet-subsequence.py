class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        i=j=float('inf')
        for num in arr:
            if num<=i: i=num
            elif num<=j: j=num
            else: return True
        return False