from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
I'm Rasel Sarker, a Computer Science and Engineering undergraduate 
student with strong knowledge in Machine Learning, NLP, Deep Learning,
and scalable automation using LLMs and LangChain. With hands-on 
experience in projects and active involvement in research.


I’ve developed custom algorithms and contributed to multiple 
papers—transforming innovative ideas into impactful solutions 
and building intelligent, real-world AI systems.
"""

# Recursive_Character_TextSplitter===========================
splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 300,   # chunkviz.up.railway.app
    chunk_overlap = 0,
)

chunks = splitter.split_text(text)

print(chunks)

# print(type(text))
# print(len(text))
# print(chunks[0].page_content)
# print(chunks[0].metadata)