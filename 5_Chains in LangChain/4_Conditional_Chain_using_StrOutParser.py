from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into possitive or negative \n {feedback}',
    input_variables = ['feedback']
)

chain = prompt1 | model | parser

result = chain.invoke({'feedback':'The smartphone is really amazing'})

print(result)

# Showing Chain
chain.get_graph().print_ascii()