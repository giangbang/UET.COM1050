from week1.p1 import solution

def test_hello_world(capsys):
    solution()
    captured = capsys.readouterr()

    assert captured.out == "Hello, World!\n"