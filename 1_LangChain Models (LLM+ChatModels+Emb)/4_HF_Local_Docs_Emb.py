from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    'What is the difference between overfitting and underfitting in machine learning?',
    'How does a convolutional neural network (CNN) extract features from an image?',
    'What is the role of the activation function in a neural network?'
]

result = embedding.embed_documents(documents)

print(str(result))