import types


def fn():
    pass

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        pass


if __name__ == '__main__':
    print(type(123) == int)
    print(type('abc') == str)

    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)

    isinstance('a', str)
    isinstance(123, int)
    isinstance(b'a', bytes)

    isinstance([1, 2, 3], (list, tuple))
    isinstance((1, 2, 3), (list, tuple))

    print(dir('abv'))

    obj = MyObject()
    hasattr(obj, 'x')  # 有属性'x'吗？ true
    hasattr(obj, 'y')  # 有属性'y'吗？ false
    setattr(obj, 'y', 19)  # 设置一个属性'y'
    hasattr(obj, 'y')  # 有属性'y'吗？ true
    getattr(obj, 'y') # 获取属性'y'

    hasattr(obj, 'power')  # 有属性'power'吗？ true
    getattr(obj, 'power')  # 获取属性'power'
    fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn

    pass