import pytest

from leetcode.graphs.models import TreeNode
from leetcode.graphs.utils import build_tree


def max_length(node: TreeNode):
    if node is None:
        return 0
    left = max_length(node.left)
    right = max_length(node.right)

    return 1 + max(left, right)

# Top-down: recomputes heights at every node - Time: O(n^2) worst case, Space: O(h)
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

# Bottom-up with -1 sentinel: each node visited once - Time: O(n), Space: O(h)
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


@pytest.mark.parametrize("solve", [balance_of_binary_tree, balance_of_binary_tree_sentinel])
@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
        ([1], True),
    ],
)
def test_is_balanced(solve, values, expected):
    assert solve(build_tree(values)) is expected