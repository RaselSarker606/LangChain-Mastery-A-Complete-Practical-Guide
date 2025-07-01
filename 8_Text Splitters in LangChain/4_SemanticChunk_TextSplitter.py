from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

text = """
Farmers were working hard in the field, preparing the soil and planting seeds for the next season. 
The sun was bright and the air  smelled of rarth and fresh grass.
The Bangladesh Premier League (BPL) is the biggest cricket league in the world.
People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates
fear in cities and villages. When such attacks happen, they leave behind pain and sasness.
To fight terrorism, we need strong laws, alert security forces, and support from people 
who care about peace and safety.
"""

# Semantic_Chunker_TextSplitter===========================
semantic = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

result = semantic.create_documents([text])

print(result)

# print(type(text))
# print(len(text))
# print(chunks[0].page_content)
# print(chunks[0].metadata)