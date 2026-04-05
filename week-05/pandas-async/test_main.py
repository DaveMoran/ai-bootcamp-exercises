import asyncio
from datetime import datetime
from unittest.mock import AsyncMock, patch, MagicMock

import pandas as pd
import pytest

from main import (
    LogEntry,
    analyze_logs,
    entries_to_dataframe,
    parse_log_line,
    process_multiple_logs,
)


# ---------------------------------------------------------------------------
# test_parse_log_line
# ---------------------------------------------------------------------------

def test_parse_log_line_valid():
    line = "2026-02-05 10:15:20 [WARN] api: Message 184 (498ms)"
    entry = asyncio.run(parse_log_line(line))

    assert entry is not None
    assert entry.timestamp == datetime(2026, 2, 5, 10, 15, 20)
    assert entry.level == "WARN"
    assert entry.source == "api"
    assert entry.message == "Message 184"
    assert entry.response_time == 498


def test_parse_log_line_malformed():
    line = "this is not a log line at all"
    entry = asyncio.run(parse_log_line(line))
    assert entry is None


def test_parse_log_line_returns_none_for_empty():
    entry = asyncio.run(parse_log_line(""))
    assert entry is None


# ---------------------------------------------------------------------------
# test_entries_to_dataframe
# ---------------------------------------------------------------------------

def _make_entries():
    return [
        LogEntry(datetime(2026, 1, 1, 0, 0, 0), "INFO", "api", "msg 1", 100),
        LogEntry(datetime(2026, 1, 1, 0, 1, 0), "ERROR", "db", "msg 2", 200),
        LogEntry(datetime(2026, 1, 1, 0, 2, 0), "WARN", "cache", "msg 3", 150),
    ]


def test_entries_to_dataframe_shape():
    df = entries_to_dataframe(_make_entries())
    assert df.shape == (3, 5)


def test_entries_to_dataframe_dtypes():
    df = entries_to_dataframe(_make_entries())
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])
    assert pd.api.types.is_string_dtype(df["level"])
    assert df["response_time"].dtype in (int, "int64")


# ---------------------------------------------------------------------------
# test_analyze_logs
# ---------------------------------------------------------------------------

def _make_df():
    entries = [
        LogEntry(datetime(2026, 1, 1, 0, 0, 0), "INFO", "api", "msg 1", 100),
        LogEntry(datetime(2026, 1, 1, 0, 1, 0), "ERROR", "db", "msg 2", 500),
        LogEntry(datetime(2026, 1, 1, 0, 2, 0), "ERROR", "cache", "msg 3", 300),
        LogEntry(datetime(2026, 1, 1, 0, 3, 0), "WARN", "api", "msg 4", 200),
        LogEntry(datetime(2026, 1, 1, 0, 4, 0), "INFO", "db", "msg 5", 400),
    ]
    return entries_to_dataframe(entries)


def test_analyze_logs_total_count():
    result = analyze_logs(_make_df())
    assert result["total_count"] == 5


def test_analyze_logs_error_rate():
    result = analyze_logs(_make_df())
    # 2 errors over 4 minutes = 0.5 errors/minute
    assert result["errors_per_minute"] == pytest.approx(0.5)


def test_analyze_logs_slowest_sort_order():
    result = analyze_logs(_make_df())
    slowest = result["slowest_requests"]
    times = list(slowest["response_time"])
    assert times == sorted(times, reverse=True)


# ---------------------------------------------------------------------------
# test_process_multiple_logs
# ---------------------------------------------------------------------------

FAKE_LOG_LINES = [
    "2026-02-05 10:00:00 [INFO] api: Message 1 (100ms)\n",
    "2026-02-05 10:01:00 [ERROR] db: Message 2 (200ms)\n",
]


@pytest.mark.asyncio
async def test_process_multiple_logs_combines_files():
    async def fake_read(filepath):
        return [await parse_log_line(line) for line in FAKE_LOG_LINES]

    with patch("main.read_and_parse_log", side_effect=fake_read):
        results = await process_multiple_logs(["file1.log", "file2.log", "file3.log"])

    assert len(results) == 6  # 2 entries × 3 files


@pytest.mark.asyncio
async def test_process_multiple_logs_concurrency():
    call_order = []

    async def fake_read(filepath):
        call_order.append(filepath)
        return [await parse_log_line(FAKE_LOG_LINES[0])]

    with patch("main.read_and_parse_log", side_effect=fake_read):
        await process_multiple_logs(["a.log", "b.log", "c.log"])

    # All three files were read
    assert sorted(call_order) == ["a.log", "b.log", "c.log"]
