from langchain_openai import ChatOpenAI
frim langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnaablePassthrough 

load_dotenv()

passthrough = RunnaablePassthrough()

# print(passthrough.invoke({'name':'rasel'}))
#=======================================================

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain the following joke - {text}',
    input_variables = ['text']
)


#joke chain
joke_chain = RunnableSequence(prompt1, model, parser)

# Runnable_Passthrough=========================
# Explanation chain
parallel_chain = RunnableParallel({
    'joke': RunnaablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)


result= final_chain.invoke({'topic':'AI'})

print(result)
