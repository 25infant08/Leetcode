from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        dicts = Counter(inorder(root))
        max_val = dicts.most_common()[0][1]
        res = []
        for key, val in dicts.items():
            if val == max_val:
                res.append(key)
        return res