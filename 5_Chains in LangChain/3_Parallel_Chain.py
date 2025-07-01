from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_persers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 =  ChatAnthropic(model_name='claude-3-7-sonnet-20250219')


# Notes generate =============================
prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text \n {text}',
    input_variables = ['text']
)

# Questions generate
prompt2 = PromptTemplate(
    template = 'Generate 5 short quiz question answers from the following text \n {text}',
    input_variables = ['text']
)

# Merge 
prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz questions into a single document \n notes -> {notes} and {quiz}',
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()


# Parallel Chain Start ==========================
parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Machine learning is a subset of artificial intelligence that focuses on creating algorithms capable of learning from data and making predictions without being explicitly programmed for specific tasks.
It enables systems to process large volumes of historical data, identify patterns, and predict new relationships between previously unknown data.
Machine learning is data-driven, learns from historical data to predict future outcomes, and is used in various applications such as predictive analytics, autonomous vehicles, chatbots, and other AI-based applications.
"""

result = chain.invoke({'text': text})

print(result)

# Showing Chain
chain.get_graph().print_ascii()