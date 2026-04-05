from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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
        # TODO: Implement
        pass
