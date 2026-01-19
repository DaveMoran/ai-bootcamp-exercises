import time


class retry:
    def __init__(self, max_attempts, delay):
        """Setup the arguments to pass to our decorator"""
        self.max_attempts = max_attempts
        self.delay = delay

    def __call__(self, fn):

        def custom_validation(result):
            """Custom validation logic placed here to exit out of while loop"""

        def retrying(*_args):
            """The retry function that will be run under the hood"""

            counter = 0
            while counter < self.max_attempts:
                time.sleep(self.delay)
                result = fn(*_args)
                if result:
                    return result

            raise Exception(f"Function failed after {self.max_attempts} tries")

        return retrying
