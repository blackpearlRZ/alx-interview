#!/usr/bin/python3
"""This module parses a log that's displayed
in stdin and displays its stats.
"""
import sys
import re


def printDict(total_size, occurenceDict):
    """ This function prints the dictionary of
        Status code occurrences in the parsed log
        in sorted order.
        Args:
            occurenceDict (dict): the dictionary of occurrences.
    """
    print("File size: {}".format(total_size))
    for key in sorted(occurenceDict.keys()):
        if occurenceDict[key] != 0:
            print("{}: {}".format(key, occurenceDict[key]))


count = 0
total_size = 0
occurenceDict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        parsed = line.split()
        if len(parsed) > 2:
            count += 1
            try:
                statusCode = parsed[-2]
                fileSize = int(parsed[-1])
                if statusCode in occurenceDict.keys():
                    occurenceDict[statusCode] += 1
                total_size += fileSize
                if count % 10 == 0:
                    printDict(total_size, occurenceDict)
            except Exception:
                continue
finally:
    printDict(total_size, occurenceDict)
