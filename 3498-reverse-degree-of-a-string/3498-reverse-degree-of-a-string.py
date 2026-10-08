class Solution:
    def reverseDegree(self, s: str) -> int:
        prod =0
        for i in range(len(s)):
            res = abs(123-ord(s[i]))
            ans = (i+1)*res
            prod+=ans
        return prod