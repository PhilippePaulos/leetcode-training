from leetcode.graphs.models import TreeNode


def build_tree(level_vals):
    """
    Build a binary tree from a level-order list.
    Use None for missing children.
    """
    if not level_vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in level_vals]
    kids = nodes[::-1]  # start from the end for pop()
    root = kids.pop()  # first element is the root
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root