from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder

# Chat_Template

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagePlaceholder(variable_name = 'chat_history'),
    ('human', {query})
])

chat_history = []

# Load Chat History

with open ('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

# Create Prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})
print(prompt)