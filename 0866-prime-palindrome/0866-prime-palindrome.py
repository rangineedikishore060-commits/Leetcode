class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(k: int) -> bool:
            if k < 2:
                return False
            if k in (2, 3):
                return True
            if k % 2 == 0 or k % 3 == 0:
                return False
            for d in range(5, int(k**0.5) + 1, 6):
                if k % d == 0 or k % (d + 2) == 0:
                    return False
            return True
        if 8 <= n <= 11:
            return 11
        for root in range(1, 100000):
            s = str(root)
            palindrome = int(s + s[-2::-1])
            
            if palindrome >= n and is_prime(palindrome):
                return palindrome