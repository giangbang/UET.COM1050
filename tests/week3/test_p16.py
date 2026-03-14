import pytest
from week3.p16 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("-5.8", "-5 -6 -6\n"),
        ("9.0", "9 9 9\n"),
        ("8.2", "9 8 8\n"),
        ("-7.5", "-7 -8 -8\n"),
        ("7.4", "8 7 7\n"),
    ],
)
def test_rounding(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output