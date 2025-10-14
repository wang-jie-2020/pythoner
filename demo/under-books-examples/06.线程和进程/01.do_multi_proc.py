import os
import threading
import time
from multiprocessing import Process


def run_proc(name):
    print("run proc %s (%s - %s)" % (name, os.getpid(), threading.current_thread().name))
    time.sleep(1)


def main():
    print("run main %s (%s - %s)" % ("main", os.getpid(), threading.current_thread().name))

    t = threading.Thread(target=run_proc, args=("线程",))
    t.start()

    p = Process(target=run_proc, args=("进程",))
    p.start()

if __name__ == '__main__':
    main()