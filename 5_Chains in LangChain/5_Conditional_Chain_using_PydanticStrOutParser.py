from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()


#=Pydantic===================================================
class Feedback(BaseModel):

    sentiment: Literal['possitive', 'negative'] = Field(description='Give the sentiment off the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into possitive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

chain = prompt1 | model | parser2


result = chain.invoke({'feedback':'The smartphone is really amazing'}).sentiment

print(result)

# Showing Chain-
chain.get_graph().print_ascii()