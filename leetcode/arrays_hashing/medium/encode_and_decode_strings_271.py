import pytest

def encode(strs: list[str]) -> str:
    return "".join(f"{len(s):03d}{s}" for s in strs)

def decode(s: str) -> list[str]:
    res, i = [], 0
    while i < len(s):
        length = int(s[i:i+3])
        res.append(s[i+3:i+3+length])
        i += length + 3
    return res

@pytest.mark.parametrize(
    "strings",
    [
        (["banana", "apple", "orange"]),
    ],
)
def test_top_k_frequent(strings):
    assert decode(encode(strings)) == strings
