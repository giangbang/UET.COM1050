import pytest
from week3.p11 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("3 3 3", "Tam giac deu\n"),
        ("3 3 4", "Tam giac can\n"),
        ("3 3 5", "Tam giac can\n"),
        ("1 2 4", "Khong phai tam giac\n"),
        ("0 0 0", "Khong phai tam giac\n"),
    ],
)
def test_triangle_type(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output