class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=[]
        for i in range(len(accounts)):
            cnt=0
            for j in range(len(accounts[i])):
                cnt+=accounts[i][j]
            res.append(cnt)
        return max(res)