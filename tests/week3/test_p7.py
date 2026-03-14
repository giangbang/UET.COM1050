import pytest
from week3.p7 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("4 -1", "No\n"),
        ("-5 -8", "Yes\n"),
        ("0 0", "No\n"),
        ("4 -1000", "No\n"),
        ("-121 -12", "Yes\n"),
    ],
)
def test_both_negative(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output