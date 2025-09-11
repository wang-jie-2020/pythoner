#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

if __name__ == '__main__':
    f = StringIO()
    f.write("hello")
    f.write(" ")
    f.write("world!")
    print(f.getvalue())

    # read from StringIO:
    f = StringIO("122abv\n比好\ngog")
    while True:
        s = f.readline()
        if s == "":
            break
        print(s.strip())