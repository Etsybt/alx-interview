#!/usr/bin/python3
"""
Log Parsing Script
"""

import sys
import re


def print_statistics(total_size, status_count):
    """
    Prints the total file size and
    the count of each status code in ascending order
    """
    print(f"File size: {total_size}")
    for status in sorted(status_count):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")


if __name__ == "__main__":
    pattern = re.compile(
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )

    line_counter = 0
    total_file_size = 0
    status_counts = {
        str(code): 0 for code in [
            200,
            301,
            400,
            401,
            403,
            404,
            405,
            500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = pattern.match(line)
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))

                total_file_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

                line_counter += 1
                if line_counter % 10 == 0:
                    print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_statistics(total_file_size, status_counts)
