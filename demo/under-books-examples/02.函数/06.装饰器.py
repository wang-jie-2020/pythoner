import datetime
import functools
import time

"""
    装饰器: 
        @语法糖 标记装饰器, @decorator 等价于 func = decorator(func)
        
        1.通过语法糖传递当前函数到装饰器中,在装饰器中执行逻辑,参照Aop理解
        2.其中参数的传递,也就是 wrapper(*args,**kw) 有点不太理解哪来的
            *args = 位置参数(必选或默认),可变参数
            **kw  = 关键字参数、命名关键字参数
        
        
        "如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数" = 再叠个buf
         @functools.wraps(func) FIX __name__ 
"""

# 这是最基础的模式, 有两个问题:(1) 装饰器参数 (2) __name__
def log(func):
    def wrapper(*args, **kw):
        print('%s %s():' % ('装饰器内的函数名称', func.__name__))
        return func(*args, **kw)

    return wrapper

# 解决装饰器参数
# def log2(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# 解决__name__
# def log3(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper

# 结合起来
def runtime(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log
def now():
    print(datetime.datetime.now())

@runtime('running')
def run():
    print('2024-6-4')

if __name__ == '__main__':

    t = now
    print('%s %s():' % ('装饰器外的函数名称', t.__name__))    # >>> wrapper

    r = run
    print('%s %s():' % ('装饰器外的函数名称', r.__name__))   # >>> run