import os

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", None)

SILICON_API_KEY = os.environ.get("SILICON_API_KEY", None)

DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY", None)

if __name__ == "__main__":
    print(DEEPSEEK_API_KEY,SILICON_API_KEY,DASHSCOPE_API_KEY)