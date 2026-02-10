#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

if __name__ == '__main__':
    f = BytesIO()
    f.write(b"hello")
    f.write(b" ")
    f.write(b"world!")
    print(f.getvalue())

    # read from BytesIO:
    data = "122abv\n比好\ngog".encode("utf-8")
    f = BytesIO(data)
    print(f.read())