import pytest
from week3.p2 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1 2", "2 1\n"),
        ("2 3", "3 2\n"),
        ("3 4", "4 3\n"),
        ("121212 232323", "232323 121212\n"),
        ("5 5", "5 5\n"),
    ],
)
def test_swap(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output