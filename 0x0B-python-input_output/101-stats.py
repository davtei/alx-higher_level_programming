#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics.
Each 10 lines and after a keyboard interruption (CTRL + C), prints
those statistics since the beginning."""


import sys

stats = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = parts[8]
            size = int(parts[9])
            total_size += size
            line_count += 1
            if status_code in stats:
                stats[status_code] += 1
            if line_count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(stats.keys()):
                    if stats[code] > 0:
                        print(f"{code}: {stats[code]}")
        except IndexError:
            pass
except KeyboardInterrupt:
    pass

print(f"Total file size: {total_size}")
for code in sorted(stats.keys()):
    if stats[code] > 0:
        print(f"{code}: {stats[code]}")
