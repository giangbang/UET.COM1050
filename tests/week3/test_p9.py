import pytest
from week3.p9 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("abc\na", "True\n"),
        ("a\nabc", "False\n"),
        ("hello\nhi", "True\n"),
        ("cat\ndog", "False\n"),
        ("python\ncode", "True\n"),
    ],
)
def test_string_length(monkeypatch, capsys, input_data, expected_output):
    inputs = iter(input_data.split("\n"))
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output