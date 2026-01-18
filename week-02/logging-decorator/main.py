import functools
import logging

logging.basicConfig(level=logging.DEBUG)

LOG_NAME = None
LOG_MESSAGE = None


class ast_log:
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
            self.log.log(logging.DEBUG, f"Begin Function {self.logmsg} | Args: {args}")

            self.log.log(self.level, self.logmsg)
            result = fn(*args, **kwargs)
            self.log.log(
                logging.DEBUG, f"Function {self.logname} Complete. Result: {result}"
            )
            return result

        return wrapper


@ast_log(logging.DEBUG)
def add(a, b):
    return a + b


add(2, 3)
