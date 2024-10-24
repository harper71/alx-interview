#!/usr/bin/python3
import sys
import signal


# Dictionary to store the count of each status code
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Variable to track total file size
total_size = 0
# Counter to track the number of lines
line_count = 0

def print_metrics():
    """Print the computed metrics: total size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    """Handle the keyboard interrupt (CTRL + C) and print metrics."""
    print_metrics()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            # Skip if line doesn't have enough parts
            continue


        # Extract file size and status code
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except (ValueError, IndexError):
            # Skip if file size or status code is invalid
            continue

        # Update total file size
        total_size += file_size

        # Update status code count if it's a valid one
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        # Every 10 lines, print the metrics
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
