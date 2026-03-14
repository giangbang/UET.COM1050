import pytest
from week3.p14 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2.4\n1.22", "-0.51\n"),
        ("0\n5", "Vô nghiệm\n"),
        ("0\n0", "Vô số nghiệm\n"),
        ("3\n-9", "3.00\n"),
        ("0.23\n99.1", "-430.87\n"),
    ],
)
def test_linear_equation(monkeypatch, capsys, input_data, expected_output):
    inputs = iter(input_data.split("\n"))
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output