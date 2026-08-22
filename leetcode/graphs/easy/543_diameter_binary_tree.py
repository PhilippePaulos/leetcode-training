from leetcode.graphs.models import TreeNode

def diameter_of_binary_tree(root: TreeNode) -> int:
    best = 0

    def height(node: TreeNode):
        nonlocal best
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        res = 1 + max(left, right)
        best = max(best, left + right)
        return res

    height(root)
    return best
