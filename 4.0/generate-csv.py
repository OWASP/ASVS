#!/usr/bin/env python

""" Quick and Dirty Roberto Martelloni's script to generate a CSV """

import re
import os


def area_from_filename(filename):
    filename_parts = filename.split("-")
    area_id = filename_parts[1]
    name = filename_parts[2].split(".")
    name = name[0].replace("_", " ")

    return [area_id, name]


def parse_md(filename):
    in_table = False

    for line in open(filename):
        if re.match(r"\s*\|", line):
            if re.match(r"\s*\|\s*#\s*\|", line):
                in_table = True
                continue
            if re.match(r"\|\s*:?--+:?\s*\|", line):
                continue

            if in_table:
                start = area_from_filename(filename)
                line = line.replace("*", "")
                line = line.replace('"', '""')
                line = re.split(r"\s*\|\s*", line)
                print('"' + '","'.join(start + line[1:-1]) + '"')
        else:
            in_table = False


def main():
    for file in os.listdir("./en"):
        if file.find("-V") != -1:
            parse_md("./en/" + file)


if __name__ == '__main__':
    main()
