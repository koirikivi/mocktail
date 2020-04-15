from unittest import mock

from when import when


def test_when_method_call():
    my_mock = mock.MagicMock()
    when(my_mock).some_method("foo").then_return("bar")
    assert my_mock.some_method("foo") == "bar"
    assert my_mock.some_method("baz") != "bar"
