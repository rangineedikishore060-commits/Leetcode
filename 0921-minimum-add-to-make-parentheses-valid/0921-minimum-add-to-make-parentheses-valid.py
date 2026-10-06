class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openn,close = 0,0
        for i in s:
            if i =='(':
                close+=1
            else:
                if close>0:
                    close-=1
                else:
                    openn+=1
        return openn+close