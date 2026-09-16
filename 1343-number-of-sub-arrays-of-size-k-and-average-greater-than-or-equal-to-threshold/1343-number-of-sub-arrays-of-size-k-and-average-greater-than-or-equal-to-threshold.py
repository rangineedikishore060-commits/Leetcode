class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        maxi=sum(arr[:k])
        res,cnt = maxi,0
        if res//k>=threshold:
            cnt+=1
        for i in range(k,len(arr)):
            res+=arr[i]
            res-=arr[i-k]
            if res//k>=threshold:
                cnt+=1
        return cnt
