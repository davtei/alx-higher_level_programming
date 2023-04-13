#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics.
Each 10 lines and after a keyboard interruption (CTRL + C), prints
those statistics since the beginning."""


def status_print(size, codes):
    """Function that prints the metrics."""
    print("File size: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))

if __name__ == "__main__":
    import sys


    size = 0
    count = 0
    codes = {}
    code = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                status_print(size, codes)
                count = 1
            else:
                count += 1
            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in code:
                    if codes.get(line[-2], -1) == -1:
                        codes[line[-2]] = 1
                    else:
                        codes[line[-2]] += 1
            except IndexError:
                pass
        status_print(size, codes)
    except KeyboardInterrupt:
        status_print(size, codes)
        raise
