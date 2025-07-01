from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_token=10)

result = model.invoke("Write a poem about Bangladesh")

print(result.content)