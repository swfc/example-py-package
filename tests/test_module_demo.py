from example_py_package.module_demo import print_something


def test_print_something(capsys):
    print_something("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == ""
