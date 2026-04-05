import aiofiles
import re


async def parse_log_line(line: str) -> Optional[LogEntry]:
    """
    Parse a log line into LogEntry.

    Format: "YYYY-MM-DD HH:MM:SS [LEVEL] source: message (Xms)"

    Args:
        line: Raw log line

    Returns:
        LogEntry or None if parsing fails
    """
    # TODO: Implement regex parsing
    pass


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
