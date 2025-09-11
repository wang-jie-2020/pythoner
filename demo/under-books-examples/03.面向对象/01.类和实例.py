"""
    class(base-class)   类名(基类名)

    实例并不像静态语言那样'继承'类属性，比如在静态语言中类必须实例化才有对象的概念，非静态的成员是无法被直接访问的，但在python中更像一种copy
    个人理解：
        继承实际上就是绑定了一个当前实例的dict -> 类的dict
        如果实例新增或重写属性那么就新增实例的dict中的属性，否则就直接链向类的dict

    实例对象
        类对象

"""


class Student(object):
    age = 12

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    bart = Student('Bart')
    michael = Student('Michael')

    print(bart.age) # 12
    print(michael.age) # 12
    print(Student.age)  # 12

    bart.age = 16
    print(bart.age) # 16
    print(michael.age) # 12
    print(Student.age)  # 12

    Student.age = 18
    print(bart.age) # 16
    print(michael.age) # 18
    print(Student.age)  # 18

