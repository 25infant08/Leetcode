from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                graph[first_email].append(email)
                graph[email].append(first_email)
        visited = set()
        result = []
        for email in graph:
            if email in visited:
                continue
            stack = [email]
            visited.add(email)
            component = []
            while stack:
                current = stack.pop()
                component.append(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            component.sort()
            result.append([email_to_name[email]] + component)
        return result