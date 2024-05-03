#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
"""
import sys
import re

if __name__ == '__main__':
    reg = (
        r'(\d{1,3}\.){3}\d{1,3} - '  # IP address
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '  # Timestamp
        r'"GET /projects/260 HTTP/1\.1" '  # HTTP request
        r'(?P<status_code>\d{3}) '  # Status code
        r'(?P<file_size>\d{1,4})'  # File size
    )
    while True:
        try:
            status_codes = {
                '200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0,
            }
            file_size = 0
            for i in range(10):
                input = sys.stdin.readline()
                matches = re.search(reg, input)
                if matches:
                    res = matches.groupdict()
                    status_codes[res['status_code']] += 1
                    file_size += int(res['file_size'])
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
        finally:
            print("File size: {}".format(file_size))
            for key, item in status_codes.items():
                if item:
                    print('{}: {}'.format(key, item))
