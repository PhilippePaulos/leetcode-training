import pytest


def trap(height: list[int]) -> int:

    return 0


@pytest.mark.parametrize(
    ("height", "expected"),
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_trap(height, expected):
    assert trap(height) == expected
