import pytest
from week3.p10 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1\n2\n4\n3", "4\n"),
        ("1000\n2000\n3123\n343", "3123\n"),
        ("-1\n-1\n-1\n-1", "-1\n"),
        ("1231\n837\n12483\n123488", "123488\n"),
        ("99999\n999\n99\n9", "99999\n"),
    ],
)
def test_max_of_four(monkeypatch, capsys, input_data, expected_output):
    inputs = iter(input_data.split("\n"))
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output