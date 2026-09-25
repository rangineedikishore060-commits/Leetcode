class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(len(nums)):
            if i.bit_count()==k:
                res+=nums[i]
        return res
            