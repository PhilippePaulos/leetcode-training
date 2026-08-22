import pytest

from leetcode.graphs.models import TreeNode
from leetcode.graphs.utils import build_tree

# Recursive DFS - Time: O(n), Space: O(h) recursion stack, h = tree height
def max_depth(root: TreeNode):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + max(left, right)


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([], 0),
        ([1], 1),
        ([1, None, 2], 2),
    ],
)
def test_max_depth(values, expected):
    assert max_depth(build_tree(values)) == expected
