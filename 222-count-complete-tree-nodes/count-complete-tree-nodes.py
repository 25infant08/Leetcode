class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        left = height(root.left)
        right = height(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)