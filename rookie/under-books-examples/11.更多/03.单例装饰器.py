from functools import wraps
from symtable import Class
from threading import RLock


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Student {self.name}, age: {self.age}'.format(self=self)

    def __repr__(self):
        return 'Student {self.name}, age: {self.age}'.format(self=self)

if __name__ == '__main__':
    A = Student('A', 20)
    B = Student('B', 20)
    print(A,B,f', A==B is {A==B}')