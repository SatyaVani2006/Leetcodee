class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        sum_val = 0
        for i in nums:
            if i % 6 == 0:
                count += 1
                sum_val += i
        if count == 0:
            return 0
        else:
            return sum_val // count


