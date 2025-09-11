"""
    python 里的ThreadLocal 更加类似于c# asyncLocal 和 java TransmittableThreadLocal
        c#、java ThreadLocal 都不能传递
"""

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    # 缁戝畾ThreadLocal鐨剆tudent:
    local_school.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=("Alice",), name="Thread-A")
    t2 = threading.Thread(target=process_thread, args=("Bob",), name="Thread-B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()