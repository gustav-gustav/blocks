from time import perf_counter, strftime
from urllib.parse import urlparse
from functools import wraps, partial
from inspect import signature
import logging
import types


def conditional_decorator(decoration, member):
    def decorator(method):
        predecorated = decoration(method)
        @wraps(method)
        def wrapper(*args, **kwargs):
            self = args[0]
            condition = getattr(self, member)
            if not condition:
                return method(*args, **kwargs)
            return predecorated(*args, **kwargs)
        return wrapper
    return decorator


def timer(function):
    @wraps(function)
    def wrapper_timer(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        elapsed = float(f"{(perf_counter() - start):.2f}")
        print(f'{function.__name__!r} finished in: {elapsed}' + " "*20)
        return value
    return wrapper_timer


def typeassert(*ty_args, **ty_kwargs):
    def decorate(function):
        if not __debug__:
            return function
        sig = signature(function)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        @wraps(function)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f'Argument {name} must be {bound_types[name]}')
            return function(*args, **kwargs)
        return wrapper
    return decorate


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    logmsg = message if message else func.__name__
    log = logging.getLogger(logname)

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper


class Timer:
    def __init__(self, function):
        wraps(function)(self)
        self.function = function
        self.function_name = function.__name__

    def __call__(self, *args, **kwargs):
        try:
            start = perf_counter()
            self.value = self.function(*args, **kwargs)
            self.elapsed = float(f"{(perf_counter() - start):.2f}")
            self.string_elapsed = f"finished in: {self.elapsed}s"
            self.string = f"{self.function_name!r} {self.string_elapsed}"
            self.printer()
            return self.value
        except ConnectionError as e:
            print(e)
        except Exception as e:
            pass

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

    def printer(self):
        print(f"{self.string_elapsed}")

class ResponseTimer(Timer):
    def printer(self):
        parsed = urlparse(self.value.url)
        endpoint = parsed.netloc
        if parsed.path:
            endpoint += parsed.path
        if parsed.params:
            endpoint += parsed.params
        if parsed.query:
            endpoint += parsed.query
        endpoint = endpoint.replace("//", "/")
        print(
            f"{strftime('[%d/%m/%Y %H:%M:%S]')} {self.value.status_code}@{endpoint!r} {self.string_elapsed} ")
