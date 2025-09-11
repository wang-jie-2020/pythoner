"""
    由于按照约定命名的设置可访问性，_以及__ 会有各自不用含义，通常来说表示私有是_(不报错但是约定不要),隐藏是__(报错)，特殊用途__xx__

     __init__(self,a,b)  参构造理解,必须是如此形式,self 指向实例对象
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('bad age')

if __name__ == '__main__':
    A = Person("A", 10)
    print(A.name)
    print(A._age)  # 不会报错,但是不符合约定
    print(A.get_age())  # 正常做法

    try:
        print(A.__age)  # 会报错
    except Exception as e:
        print(e)

    try:
        A.set_age(105)
    except Exception as e:
        print(e)
