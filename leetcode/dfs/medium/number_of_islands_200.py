import pytest

# https://leetcode.com/problems/number-of-islands/

# Target: O(m * n) time, O(m * n) space
def num_islands_stack(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    num_islands = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                num_islands += 1
                grid[i][j] = '0'
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            stack.append((nr, nc))
    return num_islands

def num_islands_recursive(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def explore(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for nr, nc in ((r+1,c), (r, c+1), (r-1,c), (r, c-1)):
            explore(nr, nc)

    num_islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                num_islands += 1
                explore(i, j)
    return num_islands

@pytest.mark.parametrize("solve", [num_islands_stack, num_islands_recursive])
@pytest.mark.parametrize(
    ("grid", "expected"),
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        ([["1"]], 1),
        ([["0"]], 0),
        ([["0", "0"], ["0", "0"]], 0),
        ([["1", "1"], ["1", "1"]], 1),
        ([["1", "0"], ["0", "1"]], 2),
        (
            [
                ["1", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "1"],
            ],
            5,
        ),
        ([["1", "1", "0", "1", "0", "1", "1"]], 3),
        ([["1"], ["0"], ["1"], ["1"]], 2),
        (
            [
                ["1", "0", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"],
            ],
            1,
        ),
        (
            [
                ["1", "0", "0", "1"],
                ["1", "0", "0", "1"],
            ],
            2,
        ),
    ],
)
def test_num_islands(solve, grid, expected):
    assert solve([row[:] for row in grid]) == expected
