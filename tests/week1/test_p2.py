import pytest
from week1.p2 import solution

@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_hello_multiple(monkeypatch, capsys, name):
    monkeypatch.setattr("builtins.input", lambda: name)

    solution()

    captured = capsys.readouterr()
    assert captured.out == f"Hello {name}\n"