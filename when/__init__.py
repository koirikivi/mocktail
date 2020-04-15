from unittest.mock import Mock

__all__ = [
    'when',
    'WhenProxy',
    'CallProxy',
]


def when(mock: Mock) -> 'WhenProxy':
    """
    Shortcut for returning `WhenProxy` for a mock object.
    Provides a nice interface for mocking up method calls, ie:

        when(my_mock).some_method('foo').then_return('bar')

    :param mock: An object that derives from `unittest.mock.Mock`
    :return: A `WhenProxy` object for the mock
    """
    return WhenProxy(mock)


class WhenProxy:
    def __init__(self, mock: Mock):
        self._mock = mock

    def __getattr__(self, item):
        return WhenProxy(getattr(self._mock, item))

    def __call__(self, *args, **kwargs):
        return CallProxy(self._mock, call_args=args, call_kwargs=kwargs)


class CallProxy:
    def __init__(self, mock: Mock, call_args, call_kwargs):
        self._mock = mock
        self._call_args = call_args
        self._call_kwargs = call_kwargs

    def then_return(self, value):
        default = self._mock.return_value
        existing_side_effect = self._mock.side_effect

        def side_effect(*args, **kwargs):
            if args == self._call_args and \
                    kwargs == self._call_kwargs:
                return value
            if existing_side_effect is not None:
                return existing_side_effect(*args, **kwargs)
            return default

        self._mock.side_effect = side_effect
