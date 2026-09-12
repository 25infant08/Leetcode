class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        index = {value: i for i, value in enumerate(inorder)}
        def build(left, right):
            if left > right:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            mid = index[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(inorder) - 1)