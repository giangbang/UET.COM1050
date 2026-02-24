import pytest
from week2.p2 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("8 7 8 6 9 9", "8.0\n"),
        ("8 7 6 5 9 8", "7.3\n"),
        ("5 6 7 8 9 10", "8.2\n"),
        ("3 7 8 10 6 5", "6.5\n"),
        ("4 5 2 8 10 7", "6.8\n"),
    ],
)
def test_average_of_six(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output