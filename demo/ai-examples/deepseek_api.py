import os

import requests

# 你的 DeepSeek API 密钥
API_KEY = os.environ.get("DEEPSEEK_API_KEY", None)

# DeepSeek API 的端点
API_URL = 'https://api.deepseek.com/v1/chat/completions'

# 请求头，包含 API 密钥
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# 请求体，包含你要发送的提示和其他参数
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "你好，请介绍一下你自己。"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

# 发送 POST 请求到 DeepSeek API
response = requests.post(API_URL, headers=headers, json=data)

# 检查响应状态码
if response.status_code == 200:
    # 解析响应内容
    result = response.json()
    print("生成的文本:", result['choices'][0]['message']['content'])
else:
    print("请求失败，状态码:", response.status_code)
    print("错误信息:", response.text)