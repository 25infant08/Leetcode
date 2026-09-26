from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node, par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root)
        q = deque([(target, 0)])
        visited = {target}
        result = []
        while q:
            node, dist = q.popleft()
            if dist == k:
                result.append(node.val)
                continue
            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
        return result