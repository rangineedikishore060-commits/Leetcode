class Solution:
    def reverseDegree(self, s: str) -> int:
        prod =0
        for i in range(len(s)):
            prod+= (i+1) * (123 - ord(s[i]))
        return prod