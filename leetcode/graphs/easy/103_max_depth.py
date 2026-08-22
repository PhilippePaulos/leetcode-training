from leetcode.graphs.models import TreeNode

def max_depth(root: TreeNode):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + max(left, right)
