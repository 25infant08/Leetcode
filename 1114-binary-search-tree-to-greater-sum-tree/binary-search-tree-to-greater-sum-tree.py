class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = [0]
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            node.val += sum[0]
            sum[0] = node.val
            dfs(node.left)
        dfs(root)
        return root