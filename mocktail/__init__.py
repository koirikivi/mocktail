from abc import ABCMeta, abstractmethod
import itertools
from unittest.mock import Mock

__all__ = [
    'when',
    'WhenProxy',
    'CallProxy',
    'Matcher',
    'Any',
]


def when(mock: Mock) -> 'WhenProxy':
    """
    Shortcut for returning `WhenProxy` for a mock object.
    Provides a nice interface for mocking up method calls, ie:

        mocktail(my_mock).some_method('foo').then_return('bar')

    :param mock: An object that derives from `unittest.mock.Mock`
    :return: A `WhenProxy` object for the mock
    """
    return WhenProxy(mock)


class WhenProxy:
    def __init__(self, mock: Mock):
        self._mock = mock

    def __getattr__(self, item) -> 'WhenProxy':
        return WhenProxy(getattr(self._mock, item))

    def __call__(self, *args, **kwargs) -> 'CallProxy':
        return CallProxy(self._mock, match_args=args, match_kwargs=kwargs)


class CallProxy:
    def __init__(self, mock: Mock, match_args, match_kwargs):
        self._mock = mock
        self._match_args = match_args
        self._match_kwargs = match_kwargs
        self._has_matchers = any(
            isinstance(arg, Matcher)
            for arg in
            itertools.chain(match_args, match_kwargs.values())
        )

    def then_return(self, value):
        default = self._mock.return_value
        existing_side_effect = self._mock.side_effect

        def side_effect(*args, **kwargs):
            if self._check_call_match(args, kwargs):
                return value
            if existing_side_effect is not None:
                return existing_side_effect(*args, **kwargs)
            return default

        self._mock.side_effect = side_effect

    def _check_call_match(self, args, kwargs):
        if self._has_matchers:
            if len(args) != len(self._match_args) or len(kwargs) != len(self._match_kwargs):
                return False
            if set(kwargs.keys()) != set(self._match_kwargs.keys()):
                return False
            for arg, match_arg in zip(args, self._match_args):
                if isinstance(match_arg, Matcher):
                    if not match_arg.matches(arg):
                        return False
                else:
                    if arg != match_arg:
                        return False
            for key in kwargs.keys():
                kwarg = kwargs[key]
                match_kwarg = self._match_kwargs[key]
                if isinstance(match_kwarg, Matcher):
                    if not match_kwarg.matches(kwarg):
                        return False
                else:
                    if kwarg != match_kwarg:
                        return False
            return True
        else:
            return args == self._match_args and kwargs == self._match_kwargs


class Matcher(metaclass=ABCMeta):
    @abstractmethod
    def matches(self, value):
        ...


class Any(Matcher):
    def __init__(self, type=None):
        self._type = type

    def matches(self, value):
        if self._type:
            return isinstance(value, self._type)
        else:
            return True
