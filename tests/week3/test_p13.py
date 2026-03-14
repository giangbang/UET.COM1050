import pytest
from week3.p13 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("40", "60000\n"),
        ("70", "115000\n"),
        ("120", "235000\n"),
        ("0", "0\n"),
        ("100", "175000\n"),
    ],
)
def test_electric_bill(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output