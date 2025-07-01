from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from langchain_community.document_loaders import CSVLoader

# CSV_Loader========================
loader = CSVLoader(file_path='5_train.csv')
docs = loader.load()

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Write a summary for the following - {text}',
    input_variables = ['text']
)

chain = prompt | model | parser

result = chain.invoke({'text': docs[0].page_content})

print(result)

# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)