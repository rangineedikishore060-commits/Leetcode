def summ(n):
    ans=0
    while n>0:
        ans+=n%10
        n//=10
    return ans
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        flag=0
        for i in range(len(nums)):
            # if i==nums[i]:
            #     return i
            if i==summ(nums[i]):
                return i
        return -1