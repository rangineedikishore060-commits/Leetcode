def binaryconvert(n,b):
    res=[]
    while n>0:
        r = n%b
        res.append(r)
        n//=b
    return res
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            res = binaryconvert(n,i)
            if res!=res[::-1]:
                return False
        return True