from week2.p1 import solution

import pytest

@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "5 2",
            "5 + 2 = 7\n"
            "5 - 2 = 3\n"
            "5 * 2 = 10\n"
            "5 // 2 =  2\n"
            "5 % 2 = 1\n"
            "5/2 = 2.50\n"
        ),
        (
            "10 3",
            "10 + 3 = 13\n"
            "10 - 3 = 7\n"
            "10 * 3 = 30\n"
            "10 // 3 =  3\n"
            "10 % 3 = 1\n"
            "10/3 = 3.33\n"
        ),
        (
            "8 4",
            "8 + 4 = 12\n"
            "8 - 4 = 4\n"
            "8 * 4 = 32\n"
            "8 // 4 =  2\n"
            "8 % 4 = 0\n"
            "8/4 = 2.00\n"
        ),
    ],
)
def test_mod_and_div(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output