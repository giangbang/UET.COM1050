import pytest
from week3.p6 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2", "Even\n"),
        ("3", "Odd\n"),
        ("4", "Even\n"),
        ("5", "Odd\n"),
        ("6", "Even\n"),
    ],
)
def test_even_odd(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output