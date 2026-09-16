class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxi = sum(nums[:k])
        res = maxi
        for i in range(k,len(nums)):
            res += nums[i]
            res -= nums[i-k]
            maxi = max(maxi,res)
        return maxi/k