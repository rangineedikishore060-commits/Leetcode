class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        k=0
        for i in range(len(nums)):
            if i%2==0:
                res.append(nums[k])
                k+=1
            else:
                res.append(nums[n])
                n+=1
        return res