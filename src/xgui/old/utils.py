import functools
import importlib
from collections import abc


class DummyClass(object):
    def __init__(self, *args, **kwargs):
        pass


def dummy_function(*args, **kwargs):
    pass


def requires_module(
    module: str, package: str = None, silent: bool = False
) -> abc.Callable:
    """This is a copy from bd103.decorators.

    Remove this when xGUI's minimum Python version is 3.9 or greater.
    """

    def decorator(func: abc.Callable) -> abc.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if importlib.util.find_spec(module, package=package):
                return func(*args, **kwargs)
            elif not silent:
                if package is None:
                    raise ModuleNotFoundError(
                        f"{repr(func)} requires module {module} to run"
                    )
                else:
                    raise ModuleNotFoundError(
                        f"{repr(func)} requires module {module} from package {package} to run"
                    )

        return wrapper

    return decorator