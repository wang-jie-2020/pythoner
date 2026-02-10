"""
    __slots__: 限制实例的属性
    class 中仍旧可以有其他属性, 但它们是read-only;
    class 中不存在的属性, 则会报错

    在继承中, 如果子类不声明则不会继承父类的slot
"""
class Student(object):
    __slots__ = ("name", "age")
    grade = '1'

class GraduateStudent(Student):
    pass

class UnGraduateStudent(Student):
    __slots__ = ()
    aabbcc = '1'

if __name__ == '__main__':

    s = Student()
    s.name = "Michael"
    s.age = 25
    try:
        s.score = 99
    except AttributeError as e:
        print("AttributeError:", e)  # ERROR: AttributeError: 'Student' object has no attribute 'score'

    try:
        print(s.grade)
        s.grade = '2'       # ERROR: 'Student' object attribute 'grade' is read-only
    except AttributeError as e:
        print("AttributeError:", e)

    g = GraduateStudent()
    g.score = 99
    print("g.score =", g.score)


    u = UnGraduateStudent()
    try:
        u.score = 99
    except AttributeError as e:
        print("AttributeError:", e)  # 'UnGraduateStudent' object has no attribute 'score'

    try:
        print(u.aabbcc)
        u.aabbcc = '2'
    except AttributeError as e:
        print("AttributeError:", e) # 'UnGraduateStudent' object attribute 'aabbcc' is read-only