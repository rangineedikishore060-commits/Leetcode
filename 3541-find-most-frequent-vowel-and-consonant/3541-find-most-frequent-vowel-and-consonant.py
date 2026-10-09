class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq1 = {}
        freq2 = {}
        for i in range(len(s)):
            if s[i] in 'aeiou':
                if s[i] not in freq1:
                    freq1[s[i]]=1
                else:
                    freq1[s[i]]+=1
            else:
                if s[i] not in freq2:
                    freq2[s[i]] =1
                else:
                    freq2[s[i]]+=1
        return max(freq1.values(),default=0)+max(freq2.values(),default=0)