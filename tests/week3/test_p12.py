import pytest
from week3.p12 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2000", "Yes\n"),
        ("2004", "Yes\n"),
        ("1900", "No\n"),
        ("2025", "No\n"),
        ("2024", "Yes\n"),
    ],
)
def test_leap_year(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output