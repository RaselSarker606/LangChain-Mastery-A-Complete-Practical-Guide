from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    'What is the difference between overfitting and underfitting in machine learning?',
    'How does a convolutional neural network (CNN) extract features from an image?',
    'What is the role of the activation function in a neural network?'
]

result = embedding.embed_documents(documents")

print(str(result))