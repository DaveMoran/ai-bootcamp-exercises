import csv
from datetime import datetime, timedelta

with open("exercises/sample_data/logs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "level", "source", "message", "response_time"])

    base_time = datetime(2026, 2, 5, 10, 0, 0)
    for i in range(1000):
        timestamp = base_time + timedelta(seconds=i * 10)
        level = "ERROR" if i % 50 == 0 else ("WARN" if i % 10 == 0 else "INFO")
        source = f"service-{i % 5}"
        message = f"Message {i}"
        response_time = 100 + (i % 200)

        writer.writerow([timestamp, level, source, message, response_time])
