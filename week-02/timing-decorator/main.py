import time

DEFAULT_FMT = "[time | 0.0s] name(*args) -> result"


class ast_timing:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt
