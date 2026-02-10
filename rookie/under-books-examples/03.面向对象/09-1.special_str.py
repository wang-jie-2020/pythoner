"""
    __str__()
    __repr__()

    相当于重写ToString()
"""
class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object (name: %s)" % self.name

    __repr__ = __str__

if __name__ == '__main__':
    print(Student("Michael"))