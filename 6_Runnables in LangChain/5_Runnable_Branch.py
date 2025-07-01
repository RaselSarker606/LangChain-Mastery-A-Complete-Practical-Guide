from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnaablePassthrough, RunnableBranch

model = ChatOpenAI()
parser = StrOutputParser()
passthrough = RunnaablePassthrough()

prompt1 = PromptTemplate(
    template= 'Write a detail report about {topic}',
    input_variables= ['topic']
)

# Report chain
report_chain = RunnableSequence(prompt1, model, parser)

# Runnable_Branch===report summarize condition=========================

prompt2 = PromptTemplate(
    template = 'Summarize the following text - {text}',
    input_variables = ['text']
)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>150,RunnableSequence(prompt2, model, parser),
    RunnaablePassthrough()
)

final_chain = RunnableSequence(report_chain,branch_chain)

result = final_chain.invoke({'topic':'Israil vs Palestine'})

print(result)