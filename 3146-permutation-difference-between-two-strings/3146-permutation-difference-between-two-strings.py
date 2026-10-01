class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        l = list(t)
        summ=0
        for i in range(len(s)):
            summ+=abs(i-l.index(s[i]))
        return summ