class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is not None and curr.val <= prev:
                return False
            prev = curr.val
            curr = curr.right
        return True