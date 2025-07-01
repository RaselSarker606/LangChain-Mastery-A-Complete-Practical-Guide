from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parser import StrOutputParser
from dotenv import load_dotenv()

from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Generate a facebook post about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a linkedin post about {topic}',
    input_variables = ['topic']
)


# Runnable_parallel
parallel_chain = RunnableParallel({
    'facebook': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result= parallel_chain.invoke({'topic':'AI'})

print(result)
