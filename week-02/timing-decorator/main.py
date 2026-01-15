import time

DEFAULT_FMT = "[time | 0.0s] name(*args) -> result"


class ast_timing:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, fn):
        def timestamp(*_args):
            start_time = time.perf_counter()
            _result = fn(*_args)
            time_taken = time.perf_counter() - start_time
            fn_name = fn.__name__
            args = ", ".join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return timestamp
