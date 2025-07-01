from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromtTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it"
    task = "text-generation"
)

model = ChatHuggingFace(lmm=lmm)

# 1st prompt -> 
template1 = PromtTemplate(
    template = 'Write a detailed report on {topic}',
    input_variable = ['topic']
)

# 2nd prompt ->
template2 = PromtTemplate(
    template = 'Write a 5 line summary on the following text. /n{text}',
    input_variable = ['text']
)

promt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(promt1)

promt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)

print(result2.content)