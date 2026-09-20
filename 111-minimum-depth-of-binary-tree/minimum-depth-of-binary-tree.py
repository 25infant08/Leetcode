from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root,1)])
        while queue:
            current,depth = queue.popleft()
            if current.left is None and current.right is None:
                return depth
            if current.left:
                queue.append((current.left, depth+1))
            if current.right:
                queue.append((current.right,depth+1))