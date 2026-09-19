class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        z = [0] * n
        
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(z[i - l], r - i + 1)
            while i + z[i] < n and word[z[i]] == word[i + z[i]]:
                z[i] += 1
            if i % k == 0 and z[i] == n - i:
                return i // k
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
            
        
        return ceil(n / k)