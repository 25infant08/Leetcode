class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
        if k <= len(factors):
            return factors[k - 1]
        k -= len(factors)
        for i in range(len(factors) - 1, -1, -1):
            factor = n // factors[i]
            if factor != factors[i]:
                k -= 1
                if k == 0:
                    return factor
        return -1