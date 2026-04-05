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
            log_entries.append(await parse_log_line(line))

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
    print(df)
    return {
        'total_count': 0,
        'level_distribution': 0,
        'avg_response_time': 0,
        'errors_per_minute': 0,
        'slowest_requests': []
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
    print(results)
    # Read 1500 total log entries

    # Analysis Results:
    # -----------------
    # Total logs: 1500
    # Level distribution:
    # INFO: 1050 (70.0%)
    # WARN: 300 (20.0%)
    # ERROR: 150 (10.0%)

    # Performance:
    # Average response time: 275ms
    # Error rate: 1.5 errors/minute

    # Slowest requests:
    # 1. 2026-02-05 10:15:20 [WARN] api: Message 184 (498ms)
    # 2. 2026-02-05 10:23:45 [ERROR] db: Message 285 (497ms)
    # 3. 2026-02-05 10:31:10 [INFO] cache: Message 374 (496ms)
    # 4. 2026-02-05 10:42:55 [WARN] queue: Message 515 (495ms)
    # 5. 2026-02-05 10:55:30 [ERROR] worker: Message 666 (494ms)


if __name__ == "__main__":
    asyncio.run(main())
