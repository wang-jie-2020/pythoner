import pickle

if __name__ == '__main__':
    d = dict(name="Bob", age=20, score=88)
    data = pickle.dumps(d)
    print(data)

    reborn = pickle.loads(data)
    print(reborn)