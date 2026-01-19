from main import retry
from unittest.mock import patch


@retry(max_attempts=3, delay=1)
def divide(a, b):
    return a / b


def test_working_function_no_retry():
    with patch("main.time.sleep") as mock_sleep:
        result = divide(4, 2)
        assert result == 2
        mock_sleep.assert_not_called()
