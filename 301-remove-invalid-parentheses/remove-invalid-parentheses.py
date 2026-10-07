class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = set()
        def dfs(i, l, r, b, path):
            if i == len(s):
                if l == r == b == 0:
                    ans.add(''.join(path))
                return
            c = s[i]
            if c == '(':
                if l:
                    dfs(i + 1, l - 1, r, b, path)
                path.append(c)
                dfs(i + 1, l, r, b + 1, path)
                path.pop()
            elif c == ')':
                if r:
                    dfs(i + 1, l, r - 1, b, path)
                if b:
                    path.append(c)
                    dfs(i + 1, l, r, b - 1, path)
                    path.pop()
            else:
                path.append(c)
                dfs(i + 1, l, r, b, path)
                path.pop()
        dfs(0, l, r, 0, [])
        return list(ans)