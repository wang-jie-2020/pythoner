import requests

if __name__ == '__main__':
    r = requests.get('https://jsonplaceholder.typicode.com/users/1')
    print(r.status_code)
    print(r.headers)
    print(r.encoding)
    print(r.text)
    print(r.content)
    print(r.json())

    r = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId': 1})
    print(r.content)


# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# r.text
#
# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#
# # requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON
#
# # 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)
#
# # 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
#
# r.headers
#
# # requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
# r.cookies['ts']
#
#
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)