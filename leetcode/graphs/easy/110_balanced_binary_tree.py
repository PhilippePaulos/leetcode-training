from leetcode.graphs.models import TreeNode


def max_length(node: TreeNode):
    if node is None:
        return 0
    left = max_length(node.left)
    right = max_length(node.right)

    return 1 + max(left, right)

def balance_of_binary_tree(root: TreeNode) -> bool:

    def is_balanced(node: TreeNode) -> bool:
        if node is None:
            return True
        left = max_length(node.left)
        right = max_length(node.right)
        if abs(left - right) > 1:
            return False
        return is_balanced(node.left) and is_balanced(node.right)

    return is_balanced(root)

def balance_of_binary_tree_sentinel(root: TreeNode) -> bool:

    def height(node: TreeNode) -> int:
        if node is None:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(root) != -1