from collections import defaultdict

import pytest


def is_valid_sudoku(board: list[list[str]]) -> bool:
    lignes = [set() for _ in range(9)]
    colonnes = [set() for _ in range(9)]
    grilles = defaultdict(set)
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val  == ".":
                continue
            val = int(val)
            if val in lignes[i]:
                return False
            elif val in colonnes[j]:
                return False
            elif val in grilles[i // 3, j // 3]:
                return False
            else:
                colonnes[j].add(val)
                lignes[i].add(val)
                grilles[i // 3, j // 3].add(val)
    return True



VALID_BOARD = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# same board but with two "8" in the first column
INVALID_BOARD = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# duplicate "1" inside the top-left 3x3 box, but rows and columns are fine
INVALID_BOX_BOARD = [
    ["1", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]

EMPTY_BOARD = [["." for _ in range(9)] for _ in range(9)]


@pytest.mark.parametrize(
    ("board", "expected"),
    [
        (VALID_BOARD, True),
        (INVALID_BOARD, False),
        (INVALID_BOX_BOARD, False),
        (EMPTY_BOARD, True),
    ],
)
def test_is_valid_sudoku(board, expected):
    assert is_valid_sudoku(board) == expected
