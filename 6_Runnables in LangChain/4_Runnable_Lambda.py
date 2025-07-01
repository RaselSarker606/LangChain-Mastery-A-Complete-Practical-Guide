from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnaablePassthrough, RunnableLambda

model = ChatOpenAI()
parser = StrOutputParser()
passthrough = RunnaablePassthrough()

prompt1 = PromptTemplate(
    template= 'Write a joke about {topic}',
    input_variables= ['topic']
)

# joke chain
joke_chain = RunnableSequence(prompt1, model, parser)

# Runnable_lambda======================================
# Explanation_WordCount chain
parallel_chain = RunnableParallel(
    'joke': RunnaablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split()))
)

# Final chain
final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

print(result)


