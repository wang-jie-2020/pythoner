"""
    动态属性, 它在某些情况下有用, 比如不必关注属性到底是干什么的, 只是有个属性而已, 都符合一定的规则
"""
class Student(object):

    def __init__(self):
        self.name = "Michael"

    def __getattr__(self, attr):
        if attr == "score":
            return 99
        if attr == "age":
            return lambda: 25
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

if __name__ == '__main__':
    s = Student()
    print(s.name)
    print(s.score)
    print(s.age())
    # AttributeError: 'Student' object has no attribute 'grade'
    print(s.grade)