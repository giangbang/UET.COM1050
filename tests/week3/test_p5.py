import pytest
from week3.p5 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2 3", "1\n"),
        ("2323 45", "52\n"),
        ("67426 11", "6130\n"),
        ("7553 764", "10\n"),
        ("2442 2", "1221\n"),
    ],
)
def test_ceil_division(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output