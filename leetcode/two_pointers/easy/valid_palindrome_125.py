import pytest

# 0(n), O(1) space
def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) -1
    while i < j:
        while i < j and not s[i].isalnum():
            i +=1
        while i < j and not s[j].isalnum():
            j -=1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("0P", False),
        ("ab_a", True),
        ("Madam, I'm Adam", True),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected
