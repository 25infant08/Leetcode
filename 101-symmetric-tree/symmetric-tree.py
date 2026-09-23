class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return check(left.left, right.right) and check(left.right, right.left)
        return check(root.left, root.right)