#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics.
Each 10 lines and after a keyboard interruption (CTRL + C), prints
those statistics since the beginning."""


import sys

total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin):
        pts = line.split()
        if len(pts) != 7:
            continue
        ip_address, date, method, path, protocol, status_code, file_size = pts

        total_size += int(file_size)

        if status_code not in status_counts:
            status_counts[status_code] = 0
        status_counts[status_code] += 1

        if i > 0 and i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
