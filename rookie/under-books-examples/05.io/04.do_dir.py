#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

if __name__ == '__main__':

    ## 系统
    print(os.name)
    # print(os.uname())   # windows 上不提供

    ## ENV
    print(os.environ)
    print(os.environ.get('GOPATH'))

    # 查看当前目录的绝对路径:
    print(os.path.abspath('.'))

    print(os.path.join(os.path.abspath('.'), 'demo'))
    os.mkdir(os.path.join(os.path.abspath('.'), 'demo'))
    os.rmdir(os.path.join(os.path.abspath('.'), 'demo'))

    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

    print("      Size     Last Modified  Name")
    for f in os.listdir(os.path.abspath(".")):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M")
        flag = "/" if os.path.isdir(f) else ""
        print("%10d  %s  %s%s" % (fsize, mtime, f, flag))