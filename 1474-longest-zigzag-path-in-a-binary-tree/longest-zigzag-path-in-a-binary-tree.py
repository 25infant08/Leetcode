class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, left, right):
            nonlocal ans
            if not node:
                return
            ans = max(ans, left, right)
            dfs(node.left, right + 1, 0)
            dfs(node.right, 0, left + 1)
        dfs(root, 0, 0)
        return ans