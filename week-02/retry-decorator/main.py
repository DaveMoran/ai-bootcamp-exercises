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
            last_exception = None

            for attempt in range(self.max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last_exception = e

                    if attempt == self.max_attempts - 1:
                        print(f"Attempted to run function {self.max_attempts} times")

                        if isinstance(e, TypeError):
                            print(
                                "Looks like you used the wrong type of vars. Check your arguements"
                            )
                        elif isinstance(e, ZeroDivisionError):
                            print(
                                "Your second arguement is a 0, that's mathmatically impossible to do. Change it out"
                            )

                        raise
                    wait_time = self.delay * (2**attempt)
                    print(f"Attempt {attempt + 1} failed, retrying in {wait_time}s...")
                    time.sleep(wait_time)

        return retrying
