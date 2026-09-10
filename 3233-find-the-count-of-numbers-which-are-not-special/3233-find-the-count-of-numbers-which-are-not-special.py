import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        cnt=0
        for i in range(2,math.isqrt(r)+1):
            flag=0
            for j in range(2,math.isqrt(i)+1):
                if i%j==0:
                    flag=1
                    break
            if flag==0:
                squar = i*i
                if l<=squar<=r:
                    cnt+=1
        return (r-l+1)-cnt