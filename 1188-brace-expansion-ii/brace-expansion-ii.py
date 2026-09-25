class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        def multiply(a, b):
            return {x + y for x in a for y in b}
        def parse(i):
            result = set()
            current = {""}
            while i < n and expression[i] != '}':
                ch = expression[i]
                if ch == ',':
                    result |= current
                    current = {""}
                    i += 1
                elif ch == '{':
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)
                else:
                    current = multiply(current, {ch})
                    i += 1
            result |= current
            if i < n and expression[i] == '}':
                i += 1
            return result, i
        result, _ = parse(0)
        return sorted(result)