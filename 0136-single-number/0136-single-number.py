class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xo = 0
        for num in nums:
            xo ^= num
        return xo