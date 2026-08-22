import pytest

from leetcode.graphs.models import TreeNode
from leetcode.graphs.utils import build_tree

# Bottom-up DFS: track best left+right while computing heights - Time: O(n), Space: O(h)
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


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),
        ([], 0),
    ],
)
def test_diameter(values, expected):
    assert diameter_of_binary_tree(build_tree(values)) == expected
