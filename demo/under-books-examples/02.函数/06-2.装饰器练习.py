import functools
import time

def runtime(func):  # 定义一个装饰器函数叫runtime 他接受一个函数func作为参数
    def wrapper(*args, **kwargs):  # 包装函数wrapper，这里接受所有参数

        # 这里是在调用原始函数前添加的新功能
        starttime = time.time()  # 获取开始执行的时间

        # 在包装函数中调用原始函数（可以不调用）
        result = func(*args, **kwargs)  # 函数传递的参数为包装函数接受的所有参数

        # 这里是在调用原始函数后添加的新功能
        endtime = time.time()  # 获取结束执行的时间

        print(f"函数{func.__name__}运行时间：{endtime - starttime}秒")  # 输出函数运行的时间

        return result  # 返回函数运行的结果

    return wrapper


# 使用装饰器装饰一个函数，现在运行这个函数时，会运行装饰器的代码，然后再由装饰器运行这个func
# （如果装饰器不调用这个函数，而是调用别的函数，就可以替换掉原有函数的功能）
@runtime
def sleepfunc(arg1, arg2):
    time.sleep(2)
    return arg1 + arg2


if __name__ == '__main__':
    pass
