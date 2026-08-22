from leetcode.graphs.models import TreeNode

# Count the total amount of nodes
def count_nodes(root: TreeNode):
    if root is None:
        return 0
    return  1 + count_nodes(root.left) + count_nodes(root.right)

def sum_values(root: TreeNode):
    if root is None:
        return 0
    left = sum_values(root.left)
    right = sum_values(root.right)
    return root.val + left + right

def max_value(root: TreeNode):
    if root is None:
        return float('-inf')
    left = max_value(root.left)
    right = max_value(root.right)
    return max(root.val, left, right)