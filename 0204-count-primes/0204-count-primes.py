from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        li = [True] * n
        li[0] = li[1] = False  # 0 and 1 are not primes
        
        for i in range(2, int(sqrt(n)) + 1):
            if li[i]:
                for j in range(i + i, n, i):
                    li[j] = False
        
        return sum(li)
