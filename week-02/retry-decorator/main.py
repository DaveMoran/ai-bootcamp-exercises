import functools
import time


class retry:
    def __init__(self, max_attempts, delay):
        """Setup the arguments to pass to our decorator"""
        self.max_attempts = max_attempts
        self.delay = delay

    def __call__(self, fn):

        @functools.wraps(fn)
        def retrying(*args, **kwargs):
            """The retry function that will be run under the hood"""

            for attempt in range(self.max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    if attempt == self.max_attempts - 1:
                        raise
                    time.sleep(self.delay * (2**attempt))

        return retrying
