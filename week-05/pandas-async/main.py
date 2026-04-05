import aiofiles
import re

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import pandas as pd
import asyncio


@dataclass
class LogEntry:
    """Represents a single parsed log line."""

    timestamp: datetime
    level: str
    source: str
    message: str
    response_time: Optional[int] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for DataFrame."""
        return {
            "timestamp": self.timestamp,
            "level": self.level,
            "source": self.source,
            "message": self.message,
            "response_time": self.response_time,
        }

# Pre-compile the regex for performance
LOG_PATTERN = re.compile(
    r"(?P<dt>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "  # Date & Time
    r"\[(?P<level>.*?)\] "  # [LEVEL]
    r"(?P<source>\w+): "  # source:
    r"(?P<message>.*?) "  # message
    r"\((?P<timing>\d+)ms\)"  # (Xms)
)


async def parse_log_line(line: str) -> Optional[LogEntry]:
    """
    Parse a log line into LogEntry.

    Format: "YYYY-MM-DD HH:MM:SS [LEVEL] source: message (Xms)"

    Args:
        line: Raw log line

    Returns:
        LogEntry or None if parsing fails
    """
    match = LOG_PATTERN.search(line)
    if not match:
        return None

    # Extract the dictionary of named groups
    data = match.groupdict()

    return LogEntry(
        timestamp=datetime.strptime(data["dt"], "%Y-%m-%d %H:%M:%S"),
        level=data["level"],
        source=data["source"],
        message=data["message"],
        response_time=int(data["timing"]),
    )


async def read_and_parse_log(filepath: str) -> list[LogEntry]:
    """
    Read log file asynchronously and parse all lines.

    Args:
        filepath: Path to log file

    Returns:
        List of LogEntry objects
    """
    log_entries = []
    async with aiofiles.open(filepath, "r") as afp:
        async for line in afp:
            entry = await parse_log_line(line)
            if entry is not None:
                log_entries.append(entry)

    return log_entries

async def process_multiple_logs(filepaths: list[str]) -> list[LogEntry]:
    """
    Process multiple log files concurrently.

    Args:
        filepaths: List of log file paths

    Returns:
        Combined list of all LogEntry objects
    """
    # TODO: Use asyncio.gather() to read all files concurrently
    # Flatten results into single list
    coroutines = []
    for path in filepaths:
        coroutines.append(read_and_parse_log(path))

    logs = []
    for result in await asyncio.gather(*coroutines):
        logs.extend(result)

    return logs

def entries_to_dataframe(entries: list[LogEntry]) -> pd.DataFrame:
    """
    Convert LogEntry objects to DataFrame.

    Args:
        entries: List of LogEntry objects

    Returns:
        Pandas DataFrame
    """
    # TODO: Convert to list of dicts, create DataFrame
    return pd.DataFrame([entry.to_dict() for entry in entries])


def analyze_logs(df: pd.DataFrame) -> dict:
    """
    Perform analysis on logs DataFrame.

    Returns dictionary with:
    - total_count: Total number of logs
    - level_distribution: Count by level
    - avg_response_time: Average response time (if present)
    - errors_per_minute: Error rate
    - slowest_requests: Top 5 slowest requests

    Args:
        df: Logs DataFrame

    Returns:
        Analysis results dictionary
    """
    # TODO: Implement all analyses
    error_count = df[df["level"] == "ERROR"].shape[0]
    minutes = (df["timestamp"].max() - df["timestamp"].min()).total_seconds() / 60
    errors_per_minute = error_count / minutes

    return {
        "total_count": df.shape[0],
        "level_distribution": df.groupby("level").size(),
        "avg_response_time": df["response_time"].mean(),
        "errors_per_minute": errors_per_minute,
        "slowest_requests": df.sort_values("response_time", ascending=False).head(5),
    }


async def run_pipeline(filepaths: list[str]) -> dict:
    """
    Complete async pipeline: read -> parse -> DataFrame -> analyze.

    Args:
        filepaths: Log files to process

    Returns:
        Analysis results
    """
    # TODO:
    # 1. Read and parse logs (async)
    parsed_logs = await process_multiple_logs(filepaths)

    # 2. Convert to DataFrame (sync)
    entries_df = entries_to_dataframe(parsed_logs)

    # 3. Analyze (sync)
    analysis = analyze_logs(entries_df)

    # 4. Return results
    return analysis


async def main():
    files = [
        "./sample_data/app_1.log",
        "./sample_data/app_2.log",
        "./sample_data/app_3.log",
    ]
    print(f"Processing {len(files)} log files asynchronously...")

    results = await run_pipeline(files)
    print(f"Read {results['total_count']} total log entries")

    print("\nAnalysis Results:")
    print("-----------------")
    print(f"Total logs: {results['total_count']}")
    print("Level distribution:")
    print(results['level_distribution'].to_string()) # TODO - add percentage as new column

    print("\nPerformance:")
    print(f"Average response time: {results['avg_response_time']}ms")
    print(f"Error rate: {results['errors_per_minute']} errors/minute:")

    print("\nSlowest requests:")
    for idx, row in enumerate(results['slowest_requests'].itertuples(), start=1):
        print(f"{idx}. {row.timestamp} [{row.level}] {row.source}: {row.message} ({row.response_time}ms)")



if __name__ == "__main__":
    asyncio.run(main())
