import subprocess

if __name__ == '__main__':
    print("$ nslookup www.python.org")
    r = subprocess.call(["nslookup", "www.python.org"])
    print("Exit code:", r)

    print("$ nslookup")
    p = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b"set q=mx\npython.org\nexit\n")
    print(output.decode("utf-8"))
    print("Exit code:", p.returncode)