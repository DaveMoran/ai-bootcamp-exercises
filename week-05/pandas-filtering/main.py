from json import load

import pandas as pd


def load_logs(filepath: str) -> pd.DataFrame:
    """
    Load logs from CSV into DataFrame.

    Args:
        filepath: Path to CSV file

    Returns:
        DataFrame with logs
    """
    # TODO: Use pd.read_csv()
    # Parse timestamp column as datetime
    logs = pd.read_csv(filepath, parse_dates=['timestamp'])
    print(logs)
    return logs


def inspect_data(df: pd.DataFrame) -> dict:
    """
    Return basic information about the DataFrame.

    Args:
        df: Logs DataFrame

    Returns:
        Dictionary with shape, columns, dtypes
    """
    # TODO: Use df.shape, df.columns, df.dtypes
    pass


def filter_by_level(df: pd.DataFrame, level: str) -> pd.DataFrame:
    """
    Filter DataFrame to only rows with specified level.

    Args:
        df: Logs DataFrame
        level: Level to filter for

    Returns:
        Filtered DataFrame
    """
    # TODO: Use boolean indexing
    pass


def filter_by_time_range(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    """
    Filter logs within time range.

    Args:
        df: Logs DataFrame
        start: Start timestamp (string)
        end: End timestamp (string)

    Returns:
        Filtered DataFrame
    """
    # TODO: Convert strings to datetime, filter
    pass


def filter_slow_requests(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """
    Filter logs where response_time > threshold.

    Args:
        df: Logs DataFrame
        threshold: Response time threshold (ms)

    Returns:
        Filtered DataFrame
    """
    # TODO: Use boolean indexing on response_time
    pass


def count_by_level(df: pd.DataFrame) -> pd.Series:
    """
    Count logs by level.

    Args:
        df: Logs DataFrame

    Returns:
        Series with level counts
    """
    # TODO: Use df.groupby('level').size()
    pass


def average_response_time_by_source(df: pd.DataFrame) -> pd.Series:
    """
    Calculate average response time per source.

    Args:
        df: Logs DataFrame

    Returns:
        Series with source -> avg_response_time
    """
    # TODO: Use df.groupby('source')['response_time'].mean()
    pass


def find_slow_errors(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """
    Find ERROR logs with high response times.

    Args:
        df: Logs DataFrame
        threshold: Response time threshold

    Returns:
        Filtered DataFrame
    """
    # TODO: Combine multiple conditions
    pass


def main():
    print("Hello from pandas-filtering!")
    load_logs('./sample_data/logs.csv')


if __name__ == "__main__":
    main()
