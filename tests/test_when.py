from unittest import mock

from when import when


def test_when_method_call():
    my_mock = mock.MagicMock()
    when(my_mock).some_method("foo").then_return("bar")
    assert my_mock.some_method("foo") == "bar"
    assert my_mock.some_method("baz") != "bar"


def test_multiple_when_method_calls():
    my_mock = mock.MagicMock()
    when(my_mock).some_method("a").then_return("A")
    when(my_mock).some_method("b").then_return("B")
    assert my_mock.some_method("a") == "A"
    assert my_mock.some_method("b") == "B"


def test_multiple_when_method_calls_order():
    """
    Whenever multiple calls are made with the exact same arguments, test that the last call overrides the previous ones.

    This is subject to change, especially after matchers are included.
    """
    my_mock = mock.MagicMock()
    when(my_mock).some_method("a").then_return("A")
    when(my_mock).some_method("a").then_return("B")
    assert my_mock.some_method("a") == "B"
