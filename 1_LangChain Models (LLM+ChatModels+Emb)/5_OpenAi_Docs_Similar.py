from langchain_openai import OpenAIEmbedding
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    'What is the difference between overfitting and underfitting in machine learning?',
    'How does a convolutional neural network (CNN) extract features from an image?',
    'What is the role of the activation function in a neural network?'
]

query = 'What is the full form of CNN'
#----------------------------------------------------

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

#-----------------------------------------------------------------
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = (sorted(list(enumerate)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is : ", score)