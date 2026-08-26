import pytest

# Target: O(n) time, O(n) space
def is_valid(s: str) -> bool:
    closing = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
       if char in closing:
           if not stack or stack.pop() != closing[char]:
               return False
       else:
           stack.append(char)

    return not stack

@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("(", False),
        (")", False),
        ("", True),
        ("{[]}", True),
        ("((", False),
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) is expected
