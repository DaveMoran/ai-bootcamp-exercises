import aiofiles
import re

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from dateutil import parser


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
    # TODO: Use aiofiles, parse each line
    pass
