class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        v = set()
        for num in nums:
            v.add(num)
            if len(v) > 3: v.remove(min(v))
        return max(v) if len(v) < 3 else min(v)
        
