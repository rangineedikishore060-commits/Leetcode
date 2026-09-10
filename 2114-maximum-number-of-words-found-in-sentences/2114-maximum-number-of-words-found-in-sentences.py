class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = []
        for i in range(len(sentences)):
            res.append(sentences[i].count(" ")+1)
        return max(res)