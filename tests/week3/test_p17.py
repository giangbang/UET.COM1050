import pytest
from week3.p17 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("92 92 92 92", "YES\n"),
        ("3 6 9 12", "NO\n"),
        ("3 9 27 54", "NO\n"),
        ("3 6 12 24", "YES\n"),
        ("4 8 12 16", "NO\n"),
    ],
)
def test_geometric_sequence(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output