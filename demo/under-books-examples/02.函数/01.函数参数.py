def calc1(numbers):
    sum_numbers = 0
    for n in numbers:
        sum_numbers = sum_numbers + n * n
    return sum_numbers


def calc2(*numbers):
    sum_numbers = 0
    for n in numbers:
        sum_numbers = sum_numbers + n * n
    return sum_numbers


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass

    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数,我觉得可以pass
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 命名关键字参数,我觉得可以pass
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


if __name__ == '__main__':
    calc1([1, 2, 3])
    calc1((1, 2, 3, 4))

    calc2(1, 2, 3)
    calc2(1, 2, 3, 4)

    # person(name, age, **kw)
    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')

    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=extra['city'], job=extra['job'])
    person('Jack', 24, **extra)

    person2('Jack', 24, city='Beijing', job='Engineer')
    person3('Jack', 24, 1, 2, 3, city='Beijing', job='Engineer')
