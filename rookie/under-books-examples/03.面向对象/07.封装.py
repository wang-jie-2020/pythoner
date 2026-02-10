"""
    __slots__ 有点类似于编译检查,看起来很像是约束类实例的属性(注意仅当前类),更深入的解释是为了节省内存 --> 内部的__dict__ 转向了 tuple；
    __slots__ 就是一个封装概念，即关注此就可以，其他的是封装细节属性不必管；子类中 __slots__=() 也许是个好习惯?

    @property 主要描述的是一种校验（私有属性通过方法传播出去不是目的）
    @property 以及 @xxx.setter 相比而言更偏向于按照C#的字段&属性去理解，虽然形式上更类似于字段+方法；这么说是因为它切换平滑性很像，比如name属性初始无要求，
    后续有校验要求，那么在外部代码其实上不需要改成getName()这种形式，没错就是在吐槽java

    这两者中应用的属性范围是不一致的，保留__slots__按照规范不该定义_name而应该定义name，因为_name在习惯上认为是私有的
    同样的道理，@property的方法名应该是name，return _name

    我不理解的是 __slots__ 除了限制实例属性, 还限制类属性, 它是不是代表着这个类足够干净, 可修改属性都已经暴露, 不需要属性检查, 也不必考虑私有
        --> 细想也不对, 限制属性就是限制属性, 与是否暴露关系无关
"""


class Student(object):
    __slots__ = ('name', 'age')

    _score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")

        self._score = value


if __name__ == '__main__':
    s = Student()
    s.name = 'A'
    s.age = 20
    s.score = 100
