def tupleImmutable():
    classmates = ('Michael', 'Bob', 'Tracy', ['A', 'B'])
    try:
        classmates[0] = 'Adam'
        print('classmates =', classmates)
    except Exception as e:
        print(e)

    try:
        classmates[3][0] = 'X'
        classmates[3][1] = 'Y'
        print('classmates =', classmates)
    except Exception as e:
        print(e)

tupleImmutable()



#  不可变性    immutability
#   可变性     variability