"""
    Python的“file-like object“就是一种鸭子类型。

    多重继承 和 单一继承 对‘继承’的概念理解并无二致，大概率自己写代码用到它也不会冲突
    但其理念有点特殊，比如其中可能有排序问题

    DAG
    下面的例子配合 https://www.jianshu.com/p/c9a0b055947b 一起看，单看代码理解不了...
"""


# # 第一个例子
# class A(object):
#     def foo(self):
#         print('A foo')
#
#     def bar(self):
#         print('A bar')
#
#
# class B(object):
#     def foo(self):
#         print('B foo')
#
#     def bar(self):
#         print('B bar')
#
#
# class C1(A, B):
#     pass
#
#
# class C2(A, B):
#     def bar(self):
#         print('C2-bar')
#
#
# class D(C1, C2):
#     pass
#
#
# if __name__ == '__main__':
#     print(D.__mro__)    # D -- C1 -- C2 -- A -- B
#     d = D()
#     d.foo()
#     d.bar()


# 第二个例子
class A(object):
    def foo(self):
        print('A foo')

    def bar(self):
        print('A bar')


class B(object):
    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A):
    pass


class C2(B):
    def bar(self):
        print('C2-bar')


class D(C1, C2):
    pass


if __name__ == '__main__':
    print(D.__mro__)    # D -- C1 -- A -- C2 -- B
    d = D()
    d.foo()
    d.bar()
