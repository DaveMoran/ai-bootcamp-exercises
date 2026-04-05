from json import load

import pandas as pd
from dateutil import parser


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
    data = {'shape': df.shape, 'columns': df.columns, 'dtypes': df.dtypes}
    return data


def filter_by_level(df: pd.DataFrame, level: str) -> pd.DataFrame:
    """
    Filter DataFrame to only rows with specified level.

    Args:
        df: Logs DataFrame
        level: Level to filter for

    Returns:
        Filtered DataFrame
    """
    filtered_df = df.loc[df["level"] == level]
    return filtered_df


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
    filtered_df = df
    if start:
        filtered_df = df.loc[
            df["timestamp"] >= parser.parse(start)
        ]

    if end:
        filtered_df = filtered_df.loc[
            filtered_df["timestamp"] < parser.parse(end)
        ]
    return filtered_df


def filter_slow_requests(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """
    Filter logs where response_time > threshold.

    Args:
        df: Logs DataFrame
        threshold: Response time threshold (ms)

    Returns:
        Filtered DataFrame
    """
    filtered_df = df.loc[df["response_time"] > threshold]
    return filtered_df


def count_by_level(df: pd.DataFrame) -> pd.Series:
    """
    Count logs by level.

    Args:
        df: Logs DataFrame

    Returns:
        Series with level counts
    """
    # TODO: Use df.groupby('level').size()
    count = df.groupby('level').size()
    return count


def average_response_time_by_source(df: pd.DataFrame) -> pd.Series:
    """
    Calculate average response time per source.

    Args:
        df: Logs DataFrame

    Returns:
        Series with source -> avg_response_time
    """
    # TODO: Use df.groupby('source')['response_time'].mean()
    avg = df.groupby('source')['response_time'].mean()
    return avg


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
    errors = filter_by_level(df, 'ERROR')
    slow_errors = filter_slow_requests(errors, threshold)
    return slow_errors


def main():
    print("Hello from pandas-filtering!")
    logs = load_logs('./sample_data/logs.csv')
    data = inspect_data(logs)

    print(f'Dataset: {data['shape'][0]} rows, {data['shape'][1]} columns')

    # Level counts:
    # INFO     900
    # WARN      80
    # ERROR     20

    # Average response time by source:
    # service-0    149.5
    # service-1    149.6
    # service-2    149.7
    # service-3    149.8
    # service-4    149.9

    # Slow errors (>200ms): 8 rows
    


if __name__ == "__main__":
    main()
