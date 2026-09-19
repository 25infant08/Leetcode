class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        vals = [set() for _ in range(n)]
        def kmp(pattern, text):
            k = 0
            lps = [0] 
            for i in range(1, len(pattern)):
                while k and pattern[k] != pattern[i]: k = lps[k-1]
                if pattern[k] == pattern[i]: k += 1
                lps.append(k)
            k = 0
            ans = []
            for i, ch in enumerate(text): 
                while k and (k == len(pattern) or pattern[k] != ch): k = lps[k-1]
                if pattern[k] == ch: k += 1
                ans.append(k)
            return ans
        for word in words: 
            cand = kmp(word, target)
            for i, k in enumerate(cand): 
                if k: vals[i].add(k)
        dp = [inf]*(n+1)
        dp[n] = 0 
        for i in range(n-1, -1, -1): 
            for k in vals[i]:
                dp[i-k+1] = min(dp[i-k+1], 1 + dp[i+1])
        return dp[0] if dp[0] < inf else -1