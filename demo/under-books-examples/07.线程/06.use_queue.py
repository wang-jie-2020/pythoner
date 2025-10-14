import threading
from queue import Queue
import time


def worker(q):
    while True:
        item = q.get()  # 从队列中获取数据，如果队列为空，则阻塞等待
        if item is None:  # 接收到None时退出循环，表示结束工作
            break
        print(f'Processed {item}')
        q.task_done()  # 表示任务已完成，用于PriorityQueue和Queue，LifoQueue不需要此方法
    print('Worker exiting')


q = Queue()
threads = []
for i in range(2):  # 创建两个工作线程
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

# 向队列中添加任务，并启动所有线程处理这些任务
for item in range(5):
    q.put(item)
    time.sleep(1)  # 模拟耗时操作，例如数据处理或网络请求等

# 加入None到队列中，通知工作线程停止工作
for _ in range(2):  # 因为有两个工作线程，所以加入两次None即可结束所有线程的工作
    q.put(None)  # 使用None作为结束信号

for t in threads:  # 等待所有线程完成工作后退出主程序
    t.join()
