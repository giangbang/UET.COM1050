import pytest
from week5.p1 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1 1", "9\n"),
        ("2 2", "25\n"),
        ("3 3", "49\n"),
        ("0 0", "1\n"),
        ("-1 -1", "5\n"),
        ("2 1", "10\n"),
        ("-2 -1", "18\n"),
        ("1324 1121", "7006812\n"),
        ("235 356", "508248\n"),
        ("892 -289", "3180270\n"),
        ("371 -124", "549576\n"),
        ("-70 495", "981516\n"),
        ("-973 933", "3788823\n"),
        ("-445 28", "792574\n"),
        ("979 836", "3829992\n"),
        ("882 -586", "3109637\n"),
        ("-873 262", "3049652\n"),
        ("81 400", "641282\n"),
        ("-190 -213", "181454\n"),
        ("1000 -1000", "3998001\n")
    ],
)
def test_spiral_number(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output