"""
    除了上面的getattr例子, call 的场景是什么...
"""
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print("My name is %s." % self.name)

if __name__ == '__main__':
    s = Student("Michael")
    s()