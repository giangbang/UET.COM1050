import pytest
from week3.p15 import solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("9.2", "Giỏi\n"),
        ("7.5", "Khá\n"),
        ("6", "Trung bình\n"),
        ("4.9", "Yếu\n"),
        ("8", "Giỏi\n"),
    ],
)
def test_student_classification(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr("builtins.input", lambda: input_data)

    solution()

    captured = capsys.readouterr()
    assert captured.out == expected_output