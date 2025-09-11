import base64

s = base64.b64encode("231fas1".encode("utf-8"))
print(s)
d = base64.b64decode(s).decode("utf-8")
print(d)

s = base64.urlsafe_b64encode("fasg2$313 4=".encode("utf-8"))
print(s)

d = base64.urlsafe_b64decode(s).decode("utf-8")
print(d)