import concurrent.futures
import math
import multiprocessing
import os
import threading
import time

def run_proc(name):
    print("run proc %s (%s - %s)" % (name, os.getpid(), threading.current_thread().name))
    time.sleep(1)

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(run_proc, "main")
        executor.map(run_proc, "main")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(run_proc, "main")
        executor.map(run_proc, "main")

if __name__ == '__main__':
    main()