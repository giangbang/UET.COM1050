import pytest
from week3.p8 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("16\n25\n9", "No\n"),
        ("3\n4\n5", "Yes\n"),
        ("3\n2\n1", "No\n"),
        ("1\n0\n10", "No\n"),
        ("10\n11\n-12", "No\n"),
    ],
)
def test_triangle(monkeypatch, capsys, input_data, expected_output):
    inputs = iter(input_data.split("\n"))
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output