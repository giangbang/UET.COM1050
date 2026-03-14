import pytest
from week3.p3 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1", "True\n"),
        ("64", "True\n"),
        ("33554432", "True\n"),
        ("4212332", "False\n"),
        ("192", "False\n"),
    ],
)
def test_power_of_two(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output