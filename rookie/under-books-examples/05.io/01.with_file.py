from datetime import datetime

if __name__ == '__main__':
    with open("test.txt", "w") as f:
        f.write("123 ")
        f.write(datetime.now().strftime("%Y-%m-%d"))

    with open("test.txt", "r") as f:
        s = f.read()
        print("open for read...")
        print(s)

    with open("test.txt", "rb") as f:
        s = f.read()
        print("open as binary for read...")
        print(s)

    with open('test.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
        f.close()