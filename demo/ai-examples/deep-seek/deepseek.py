from llama_index.llms.deepseek import DeepSeek
import core.ApiKeys

llm = DeepSeek(model="deepseek-reasoner", api_key=core.DEEPSEEK_API_KEY)

# You might also want to set deepseek as your default llm
# from llama_index.core import Settings
# Settings.llm = llm

response = llm.complete("Is 9.9 or 9.11 bigger?")
print(response)