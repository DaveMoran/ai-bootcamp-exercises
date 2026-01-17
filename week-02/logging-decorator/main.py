import functools
import logging

LOG_NAME = None
LOG_MESSAGE = None

logging.basicConfig(level=logging.DEBUG)


class logging_decorator:
    def __init__(self, level, name=LOG_NAME, message=LOG_MESSAGE):
        self.level = level
        self.logname = name
        self.logmsg = message

    def __call__(self, fn):
        self.fn = fn
        self.logname = self.logname if self.logname else fn.__module__
        self.log = logging.getLogger(self.logname)
        self.logmsg = self.logmsg if self.logmsg else fn.__name__

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            self.log.log(self.level, self.logmsg)
            return fn(*args, **kwargs)

        return wrapper


@logging_decorator(logging.DEBUG)
def add(x, y):
    return x + y


add(2, 3)
