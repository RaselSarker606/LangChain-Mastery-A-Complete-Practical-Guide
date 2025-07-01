from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('1_computers-12-00087.pdf')

docs = loader.load()

# CharacterText_Splitter=======================
splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)

print(result[1].result_content) # result[0,1.....]=1st chunk, 2nd chunk....