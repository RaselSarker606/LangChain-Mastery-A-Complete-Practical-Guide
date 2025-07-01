from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

from langchain.schema.runnable import RunnableParallel, RunnableBranch

parser = StrOutputParser()


#=Pydantic===================================================
class Feedback(BaseModel):

    sentiment: Literal['possitive', 'negative'] = Field(description='Give the sentiment off the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into possitive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classify_chain = prompt1 | model | parser2


#=Branch_Chain=========================================
prompt2 = PromptTemplate(
    template  = "Write an appropriate response to this possitive feedback \n {feedback}",
    input_variables = ['feedback']
)

prompt2 = PromptTemplate(
    template  = "Write an appropriate response to this negative feedback \n {feedback}",
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'possitive', prompt2 | model | parser) # prompt2 triger
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser) # prompt3 triger
    lambda x: "Could not find sentiment"
)

# Final Chain=========================================
chain =  classify_chain | branch_chain

print(chain.invoke({'feedback':'This is a beautiful smartphone'}))

# Showing Chain-
chain.get_graph().print_ascii()

 