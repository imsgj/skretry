import functools


def simple_decorator(caller):
    """Turns caller into a decorator.
    Unlike decorator module, function signature is not preserved.

    :param caller: caller(f, *args, **kwargs)
    """

    def decor(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return caller(f, *args, **kwargs)

        return wrapper

    return decor


try:
    from decorator import decorator
except ImportError:
    decorator = simple_decorator
