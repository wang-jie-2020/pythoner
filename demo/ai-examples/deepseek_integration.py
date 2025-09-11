from llama_index.llms.deepseek import DeepSeek
import os

# Set up the DeepSeek class with the required model and API key
llm = DeepSeek(model="deepseek-chat", api_key=os.environ.get("DEEPSEEK_API_KEY", None))

# Call the complete method with a query
response = llm.complete("Explain the importance of low latency LLMs")

print(response)