from collections import deque
from typing import Optional

import pytest

from leetcode.graphs.models import TreeNode
from leetcode.graphs.utils import build_tree

# Recursive mirror DFS - Time: O(n), Space: O(h) recursion stack, h = tree height
def is_symmetric(root: Optional[TreeNode]) -> bool:

    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root, root)

# Iterative BFS on mirrored node pairs - Time: O(n), Space: O(n)
def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:

    if not root:
        return True

    queue = deque([(root.left, root.right)])
    while queue:
        left, right = queue.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True


@pytest.mark.parametrize("solve", [is_symmetric, is_symmetric_iterative])
@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], True),
        ([1], True),
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1, 2, 2, 3, 5, 4, 3], False),
    ],
)
def test_is_symmetric(solve, values, expected):
    assert solve(build_tree(values)) is expected
