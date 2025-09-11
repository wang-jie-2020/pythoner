"""
    tqdm
"""
import time
from tqdm import *

if __name__ == '__main__':
    #for i in tqdm(range(1000)):
    #    time.sleep(.01)    #进度条每0.1s前进一次，总时间为1000*0.1=100s

    for i in tqdm(range(10), desc='主要进度', position=0):
        for j in tqdm(range(100), desc='次要进度', position=1, leave=False):
            time.sleep(0.001)  # 模拟你的任务需要一些时间