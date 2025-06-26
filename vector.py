# from langchain_ollama import OllamaEmbeddings
# from langhchain_chroma import Chroma 
# from langchain_core.documents import Document
# import os 
# import pandas as pd

# df = pd.read_csv('Restaurant reviews.csv')
# embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# db_location = "./chroma_langchain_db"
# add_documents = not os.path.exists(db_location)

# if add_documents:
#     documents = []
#     ids = []

#     for i, row in df.iterrows():
#         document = Document(
#             page_content=row["Title"] + " " + row
#         )