#!/usr/bin/python

""" Quick and Dirty Roberto Martelloni's script to generate a CSV """

import os


def fromFilenameToArea(filename):
    splittedFilename = filename.split("-")
    id = splittedFilename[1]
    name = splittedFilename[2].split(".")
    name = name[0].replace("_", " ")

    return id, name



def parsemd(filename):

    for line in open(filename):
        if line.startswith("|"):
            if line.find("| --- |") == 0: continue
            if line.find("| # |") == 0: continue
            if line.find("|  #") == 0: continue

            start = fromFilenameToArea(filename)
            line = line.replace("*", "")
            line = line.split("|")
            print start[0] + "|",
            print start[1] + "|",
            print line[1] + "|",
            print line[2] + "|",
            print line[3] + "|",
            print line[4] + "|"


def main():
    for file in os.listdir("./en"):
        if file.find("-V") != -1:
            parsemd("./en/" + file)


if __name__ == '__main__':
    main()
