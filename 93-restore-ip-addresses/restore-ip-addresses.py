class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    result.append(".".join(parts))
                return
            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]
                if len(part) > 1 and part[0] == '0':
                    break
                if int(part) > 255:
                    break
                backtrack(j + 1, parts + [part])
        backtrack(0, [])
        return result