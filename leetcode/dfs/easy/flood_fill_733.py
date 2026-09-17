from copy import deepcopy

import pytest

# https://leetcode.com/problems/flood-fill/

# Recursive DFS - Time: O(m * n), Space: O(m * n) recursion stack (worst case)
def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    old_color = image[sr][sc]
    if color == old_color:
        return image

    def fill(sr, sc):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return

        if image[sr][sc] != old_color:
            return

        image[sr][sc] = color

        fill(sr - 1, sc)
        fill(sr + 1, sc)
        fill(sr, sc - 1)
        fill(sr, sc + 1)

    fill(sr, sc)

    return image

# Iterative DFS with an explicit stack - Time: O(m * n), Space: O(m * n)
def flood_fill_iterative(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    old_color = image[sr][sc]
    if color == old_color:
        return image

    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        if r < 0 or r >= len(image) or r < 0 or c >= len(image[0]):
            continue
        if image[r][c] != old_color:
            continue
        image[r][c] = color
        stack.append((r - 1, c))
        stack.append((r + 1, c))
        stack.append((r, c - 1))
        stack.append((r, c + 1))

    return image

@pytest.mark.parametrize("solve", [flood_fill_iterative])
@pytest.mark.parametrize(
    ("image", "sr", "sc", "color", "expected"),
    [
        (
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            1, 1, 2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        (
            [[0, 0, 0], [0, 0, 0]],
            0, 0, 0,
            [[0, 0, 0], [0, 0, 0]],
        ),
        ([[5]], 0, 0, 9, [[9]]),
        (
            [[1, 1], [1, 1]],
            0, 1, 3,
            [[3, 3], [3, 3]],
        ),
        (
            [[1, 2, 1], [2, 1, 2], [1, 2, 1]],
            1, 1, 7,
            [[1, 2, 1], [2, 7, 2], [1, 2, 1]],
        ),
        (
            [[1, 0], [0, 1]],
            0, 0, 4,
            [[4, 0], [0, 1]],
        ),
        (
            [[0, 0, 0], [0, 1, 1], [0, 1, 1]],
            2, 0, 5,
            [[5, 5, 5], [5, 1, 1], [5, 1, 1]],
        ),
        ([[2, 2, 3, 2, 2]], 0, 4, 8, [[2, 2, 3, 8, 8]]),
        ([[4], [4], [1], [4]], 0, 0, 6, [[6], [6], [1], [4]]),
    ],
)
def test_flood_fill(solve, image, sr, sc, color, expected):
    # copie profonde : la fonction peut modifier l'image en place, on protege les cas de test
    assert solve([row[:] for row in image], sr, sc, color) == expected
