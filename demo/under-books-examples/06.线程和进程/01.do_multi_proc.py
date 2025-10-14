import multiprocessing
import os
import threading
import time


def run_proc(name):
    print("run proc %s (%s - %s)" % (name, os.getpid(), threading.current_thread().name))
    time.sleep(10)


def main():
    print("run main %s (%s - %s)" % ("main", os.getpid(), threading.current_thread().name))

    t = threading.Thread(target=run_proc, args=("线程",))
    t.start()

    p = multiprocessing.Process(target=run_proc, args=("进程",))
    p.start()

if __name__ == '__main__':
    main()

"""
    有个疑问: 按照预期主进程/线程 直接结束而不是等待才对
"""