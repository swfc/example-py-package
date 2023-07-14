from example_py_package.snake import say


def test_say(capsys):
    say("hello")
    captured = capsys.readouterr()
    assert "hello" in captured.out
    assert captured.err == ""
