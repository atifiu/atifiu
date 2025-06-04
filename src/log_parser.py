"""Simple Spark log parser utilities."""

from __future__ import annotations


def parse_log_line(line: str) -> dict[str, str]:
    """Return a dictionary representation of a Spark log line.

    This is a placeholder implementation that simply splits the line
    by spaces and returns indexed fields.
    """
    parts = line.strip().split()
    return {f"field_{i}": part for i, part in enumerate(parts)}


def parse_log_file(path: str) -> list[dict[str, str]]:
    """Parse a log file and return a list of structured records."""
    records = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            records.append(parse_log_line(line))
    return records
