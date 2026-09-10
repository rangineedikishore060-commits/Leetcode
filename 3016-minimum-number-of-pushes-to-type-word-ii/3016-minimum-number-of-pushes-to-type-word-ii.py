class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in word:
            freq[i]=freq.get(i,0)+1
        l = sorted(list(freq.values()))
        cnt,ans,j=0,0,1
        for i in range(len(l)-1,-1,-1):
            ans += j*l[i]
            cnt+=1
            if cnt==8:
                j+=1
                cnt=0
        return ans