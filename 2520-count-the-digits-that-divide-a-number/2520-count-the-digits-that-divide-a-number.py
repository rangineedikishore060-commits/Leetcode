class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        cnt=0
        while num>0:
            r = num%10
            if temp%r==0:
                cnt+=1
            num//=10
        return cnt