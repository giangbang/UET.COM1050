import pytest
from week2.p3 import solution

@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2 3", "8\n"),
        ("4 5", "1024\n"),
        ("30 5", "24300000\n"),
        ("3 2", "9\n"),
        ("5 2", "25\n"),
    ],
)
def test_exponentiation(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output