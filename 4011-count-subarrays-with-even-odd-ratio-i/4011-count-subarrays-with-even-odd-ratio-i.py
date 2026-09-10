class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        temp = nums
        n = len(temp)
        cnt = 0
        for i in range(n):
            ecnt, ocnt = 0, 0
            for j in range(i, n):
                if temp[j] % 2 == 0:
                    ecnt += 1
                else:
                    ocnt += 1
                if ocnt > 0 and ecnt * b <= ocnt * a:
                    cnt += 1
        return cnt
