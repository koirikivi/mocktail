import pytest
from unittest import mock

from mocktail import (
    when,
    Any,
    Match,
)


def test_when_method_call_then_return():
    my_mock = mock.MagicMock()
    when(my_mock).some_method("foo").then_return("bar")
    assert my_mock.some_method("foo") == "bar"
    assert my_mock.some_method("baz") != "bar"


def test_when_method_call_then():
    my_mock = mock.MagicMock()
    when(my_mock).some_method("foo").then(lambda x: x + "bar")
    assert my_mock.some_method("foo") == "foobar"
    assert my_mock.some_method("baz") != "foobar"


def test_when_method_call_then_raise_error():
    my_mock = mock.MagicMock()

    def error(arg):
        raise TabError(arg)

    when(my_mock).some_method("foo").then(error)
    my_mock.some_method("baz")
    with pytest.raises(TabError):
        my_mock.some_method("foo")


def test_when_direct_call():
    my_mock = mock.MagicMock()
    when(my_mock)("o").then_return("k")
    assert my_mock("o") == "k"


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


def test_matcher_any():
    my_mock = mock.MagicMock()
    when(my_mock).foo(Any()).then_return("foo")
    assert my_mock.foo(123) == "foo"
    assert my_mock.foo() != "foo"


def test_matcher_any_type():
    my_mock = mock.MagicMock()
    when(my_mock).foo(Any(str)).then_return("foo")
    assert my_mock.foo("123") == "foo"
    assert my_mock.foo(123) != "foo"


def test_callback_matcher_basic():
    my_mock = mock.MagicMock()
    when(my_mock).foo(Match(callback=lambda x: True)).then_return("match")
    assert my_mock.foo(123) == "match"
    assert my_mock.foo(456) == "match"
    assert my_mock.foo() != "match"


def test_callback_matcher_startswitch():
    my_mock = mock.MagicMock()
    when(my_mock).foo(Match(callback=lambda x: x.startswith('foo'))).then_return("match")
    assert my_mock.foo('foobar') == "match"
    assert my_mock.foo('foo') == "match"
    assert my_mock.foo('barfoo') != "match"
    assert my_mock.foo('x') != "match"
