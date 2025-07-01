from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader

# WebBase_Loader========================
url = 'https://www.flipkart.com/apple-macbook-air'
loader = WebBaseLoader(url)
docs = loader.load()

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Answer the following question - {question} from the following text - {text}',
    input_variables = ['question','text']
)

chain = prompt | model | parser

result = chain.invoke({'question':'What is the peak brightness of this product....?','text': docs[0].page_content})

print(result)

# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)