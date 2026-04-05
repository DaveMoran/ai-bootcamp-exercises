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


async def parse_log_line(line: str) -> Optional[LogEntry]:
    """
    Parse a log line into LogEntry.

    Format: "YYYY-MM-DD HH:MM:SS [LEVEL] source: message (Xms)"

    Args:
        line: Raw log line

    Returns:
        LogEntry or None if parsing fails
    """
    datetime = re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}", line)
    if datetime:
        datetime_date = parser.parse(datetime.group(0))
    else:
        return None


    return LogEntry(datetime_date, "", "", "", 0)


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
