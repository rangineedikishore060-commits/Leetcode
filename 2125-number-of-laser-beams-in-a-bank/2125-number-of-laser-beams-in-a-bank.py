class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        cnt = 0
        for row in bank:
            devices = row.count("1")
            if devices > 0:
                cnt += prev * devices
                prev = devices
        return cnt