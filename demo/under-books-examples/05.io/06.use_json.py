"""
    "因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象" --- 这不弱智吗 ?  不可能吧...

    `json`模块有四个比较重要的函数，分别是：
        - `dump` - 将Python对象按照JSON格式序列化到文件中
        - `dumps` - 将Python对象处理成JSON格式的字符串
        - `load` - 将文件中的JSON数据反序列化成对象
        - `loads` - 将字符串的内容反序列化成Python对象

"""
import json

if __name__ == '__main__':
    d = dict(name="Bob", age=20, score=88)
    data = json.dumps(d)
    print("JSON Data is a str:", data)
    reborn = json.loads(data)
    print(reborn)

    class Student(object):

        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = score

        def __str__(self):
            return "Student object (%s, %s, %s)" % (self.name, self.age, self.score)


    s = Student("Bob", 20, 88)
    std_data = json.dumps(s, default=lambda obj: obj.__dict__)
    print("Dump Student:", std_data)
    rebuild = json.loads(std_data, object_hook=lambda d: Student(d["name"], d["age"], d["score"]))
    print(rebuild)