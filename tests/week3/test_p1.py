import pytest
from week3.p1 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1234", "4321\n"),
        ("2222", "2222\n"),
        ("5343", "3435\n"),
        ("3443", "3443\n"),
        ("1", "1\n"),
    ],
)
def test_reverse_number(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output